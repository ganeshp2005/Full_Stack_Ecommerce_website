from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Category, Product, Cart, CartItem, Order, OrderItem


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Preferences'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'seller', 'price', 'stock', 'is_active', 'featured', 'created_at')
    list_filter = ('category', 'is_active', 'featured', 'seller')
    search_fields = ('name', 'description', 'seller__username')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'stock', 'is_active', 'featured')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description', 'image')
        }),
        ('Seller Information', {
            'fields': ('seller',)
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'original_price', 'stock')
        }),
        ('Status', {
            'fields': ('is_active', 'featured')
        }),
        ('Ratings', {
            'fields': ('rating', 'reviews_count')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('added_at',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_items', 'total_price', 'updated_at')
    search_fields = ('user__username', 'id')
    inlines = [CartItemInline]
    readonly_fields = ('id', 'created_at', 'updated_at')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name', 'product_price', 'quantity', 'subtotal')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'full_name', 'total', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('order_id', 'user__username', 'full_name', 'email', 'phone')
    list_editable = ('status',)
    inlines = [OrderItemInline]
    readonly_fields = ('order_id', 'subtotal', 'shipping_cost', 'total', 'created_at', 'updated_at')
    fieldsets = (
        ('Order Info', {
            'fields': ('order_id', 'user', 'status', 'payment_method')
        }),
        ('Customer Details', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('Shipping Address', {
            'fields': ('address', 'city', 'state', 'pincode')
        }),
        ('Billing', {
            'fields': ('subtotal', 'shipping_cost', 'total')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'quantity', 'subtotal')
    list_filter = ('order__status',)
    search_fields = ('order__order_id', 'product_name')