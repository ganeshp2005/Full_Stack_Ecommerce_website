import time
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from decimal import Decimal
from .models import Category, Product, Cart, CartItem, Order, OrderItem, UserProfile
from .forms import UserRegisterForm, UserLoginForm, CheckoutForm, ProductForm


# ============ Authentication Views ============
def register_view(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}! Your account has been created successfully.')
            return redirect('store')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UserRegisterForm()

    return render(request, 'home/register.html', {'form': form, 'title': 'Create Account'})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('store')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = UserLoginForm()

    return render(request, 'home/login.html', {'form': form, 'title': 'Login'})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('store')


# ============ Store Views ============
def store(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)
    featured_products = products.filter(featured=True)[:8]

    # Search
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Sort
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'rating':
        products = products.order_by('-rating')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('name')

    context = {
        'categories': categories,
        'products': products,
        'featured_products': featured_products,
        'current_category': category_slug,
        'current_sort': sort,
        'query': query,
    }
    return render(request, 'home/store.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(category=product.category, is_active=True).exclude(id=product.id)[:4]
    in_cart = False

    cart = get_or_create_cart(request)
    if cart and cart.items.filter(product=product).exists():
        in_cart = True

    context = {
        'product': product,
        'related_products': related_products,
        'in_cart': in_cart,
    }
    return render(request, 'home/product_detail.html', context)


# ============ Cart Views ============
def get_or_create_cart(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = None

    if cart is None:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart = Cart.objects.create(user=None)
        request.session['cart_id'] = str(cart.id)

    return cart


def cart_view(request):
    cart = get_or_create_cart(request)
    context = {
        'cart': cart,
        'cart_items': cart.items.select_related('product').all() if cart else [],
        'subtotal': sum(item.subtotal for item in cart.items.all()) if cart else 0,
    }
    return render(request, 'home/cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart = get_or_create_cart(request)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        quantity = max(1, min(quantity, product.stock if product.stock > 0 else quantity))

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            new_qty = cart_item.quantity + quantity
            cart_item.quantity = min(new_qty, product.stock if product.stock > 0 else new_qty)
            cart_item.save()

        messages.success(request, f'"{product.name}" added to your cart.')
    else:
        messages.info(request, 'Invalid request.')

    return redirect('cart')


def update_cart_item(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        quantity = int(request.POST.get('quantity', 1))
        product = cart_item.product

        if quantity <= 0:
            cart_item.delete()
            messages.info(request, 'Item removed from cart.')
        else:
            cart_item.quantity = min(quantity, product.stock if product.stock > 0 else quantity)
            cart_item.save()
            messages.success(request, 'Cart updated successfully.')

    return redirect('cart')


def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        product_name = cart_item.product.name
        cart_item.delete()
        messages.success(request, f'"{product_name}" removed from cart.')

    return redirect('cart')


# ============ Checkout Views ============
@login_required
def checkout(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('product').all()

    if len(cart_items) == 0:
        messages.warning(request, 'Your cart is empty. Add some products first.')
        return redirect('cart')

    subtotal = sum(item.subtotal for item in cart_items)
    shipping = Decimal('49.00') if subtotal < Decimal('499') else Decimal('0.00')
    total = subtotal + shipping

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode'],
                subtotal=subtotal,
                shipping_cost=shipping,
                total=total,
                payment_method=form.cleaned_data['payment_method'],
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    product_name=item.product.name,
                    product_price=item.product.price,
                    quantity=item.quantity,
                    subtotal=item.subtotal,
                )
                if item.product.stock > 0:
                    item.product.stock -= item.quantity
                    item.product.save()

            cart.items.all().delete()
            request.session.pop('cart_id', None)

            messages.success(request, f'Order placed successfully! Your order ID is {order.order_id}.')
            return redirect('order_confirmation', order_id=order.order_id)
    else:
        form = CheckoutForm(initial={
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        })

    context = {
        'form': form,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    }
    return render(request, 'home/checkout.html', context)


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, order_id=order_id, user=request.user)
    return render(request, 'home/order_confirmation.html', {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'home/order_history.html', {'orders': orders})


# ============ Seller Views ============
@login_required
def seller_dashboard(request):
    """Dashboard showing seller's products and sales"""
    my_products = Product.objects.filter(seller=request.user)
    my_orders = OrderItem.objects.filter(product__seller=request.user).select_related('order', 'product')

    total_sales = sum(item.subtotal for item in my_orders)
    total_orders = my_orders.count()

    context = {
        'my_products': my_products,
        'my_orders': my_orders,
        'total_sales': total_sales,
        'total_orders': total_orders,
        'product_count': my_products.count(),
    }
    return render(request, 'home/seller_dashboard.html', context)


@login_required
def seller_add_product(request):
    """Allow any logged-in user to sell products"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.success(request, f'Your product "{product.name}" has been listed for sale!')
            return redirect('seller_dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = ProductForm()

    return render(request, 'home/seller_add_product.html', {'form': form})


@login_required
def seller_edit_product(request, product_id):
    """Edit a seller's own product"""
    product = get_object_or_404(Product, id=product_id, seller=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{product.name}" has been updated.')
            return redirect('seller_dashboard')
    else:
        form = ProductForm(instance=product)

    return render(request, 'home/seller_edit_product.html', {'form': form, 'product': product})


@login_required
def seller_delete_product(request, product_id):
    """Delete a seller's own product"""
    product = get_object_or_404(Product, id=product_id, seller=request.user)

    if request.method == 'POST':
        name = product.name
        product.delete()
        messages.success(request, f'"{name}" has been removed from your listings.')
        return redirect('seller_dashboard')

    return render(request, 'home/seller_delete_product.html', {'product': product})


# ============ User Settings Views ============
@login_required
def user_settings(request):
    """User can personalize their experience - theme, font, color"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        theme = request.POST.get('theme', 'light')
        font_size = request.POST.get('font_size', 'default')
        color_scheme = request.POST.get('color_scheme', 'orange')

        # Validate choices
        valid_themes = [choice[0] for choice in UserProfile.THEME_CHOICES]
        valid_fonts = [choice[0] for choice in UserProfile.FONT_CHOICES]
        valid_colors = [choice[0] for choice in UserProfile.COLOR_CHOICES]

        if theme in valid_themes:
            profile.theme = theme
        if font_size in valid_fonts:
            profile.font_size = font_size
        if color_scheme in valid_colors:
            profile.color_scheme = color_scheme

        profile.save()
        messages.success(request, 'Your preferences have been saved successfully!')
        return redirect('user_settings')

    return render(request, 'home/settings.html', {'profile': profile})


# ============ SQL Command Console View ============
def sql_console(request):
    """Interactive SQL Command Console to view database schema and execute custom SQL commands live."""
    query = request.POST.get('query', request.GET.get('query', 'SELECT * FROM home_product LIMIT 10;')).strip()
    results = None
    columns = []
    error = None
    execution_time = 0
    row_count = 0

    # Get schema tables and their row counts for schema browser
    table_info = []
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;")
            tables = [row[0] for row in cursor.fetchall()]
            for tbl in tables:
                cursor.execute(f"SELECT COUNT(*) FROM \"{tbl}\";")
                cnt = cursor.fetchone()[0]
                table_info.append({'name': tbl, 'count': cnt})
    except Exception as e:
        table_info = []

    # Preset sample SQL queries
    presets = [
        {"name": "📦 All Products", "icon": "fa-boxes", "sql": "SELECT id, name, price, stock, rating FROM home_product ORDER BY id DESC LIMIT 15;"},
        {"name": "📁 Categories", "icon": "fa-folder", "sql": "SELECT id, name, slug FROM home_category;"},
        {"name": "👤 Registered Users", "icon": "fa-users", "sql": "SELECT id, username, email, is_staff, date_joined FROM auth_user;"},
        {"name": "🛒 Customer Orders", "icon": "fa-shopping-bag", "sql": "SELECT order_id, full_name, total, payment_method, status, created_at FROM home_order ORDER BY created_at DESC;"},
        {"name": "🔥 Top Rated Products", "icon": "fa-star", "sql": "SELECT name, price, rating, discount_percent FROM home_product WHERE rating >= 4.5 ORDER BY rating DESC;"},
        {"name": "📊 Stock & Category Analytics", "icon": "fa-chart-pie", "sql": "SELECT c.name as category, COUNT(p.id) as total_products, SUM(p.stock) as total_stock, ROUND(AVG(p.price), 2) as avg_price FROM home_category c LEFT JOIN home_product p ON c.id = p.category_id GROUP BY c.id;"},
        {"name": "🗄️ Database Tables Schema", "icon": "fa-database", "sql": "SELECT name, type, sql FROM sqlite_master WHERE type='table' ORDER BY name;"},
        {"name": "⚡ User Profiles & Settings", "icon": "fa-sliders-h", "sql": "SELECT u.username, p.theme, p.font_size, p.color_scheme FROM auth_user u JOIN home_userprofile p ON u.id = p.user_id;"},
    ]

    if query:
        start_time = time.time()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                if cursor.description:
                    columns = [col[0] for col in cursor.description]
                    results = cursor.fetchall()
                    row_count = len(results)
                else:
                    row_count = cursor.rowcount if cursor.rowcount >= 0 else 0
                    columns = ["Status"]
                    results = [(f"SQL statement executed successfully. Rows affected: {row_count}",)]
        except Exception as e:
            error = str(e)
        execution_time = round((time.time() - start_time) * 1000, 2)

    context = {
        'query': query,
        'columns': columns,
        'results': results,
        'error': error,
        'row_count': row_count,
        'execution_time': execution_time,
        'tables': table_info,
        'presets': presets,
    }
    return render(request, 'home/sql_console.html', context)

