from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Store
    path('', views.store, name='store'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # Cart
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Checkout & Orders
    path('checkout/', views.checkout, name='checkout'),
    path('order/<str:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('my-orders/', views.order_history, name='order_history'),

    # Seller Routes
    path('sell/', views.seller_dashboard, name='seller_dashboard'),
    path('sell/add/', views.seller_add_product, name='seller_add_product'),
    path('sell/edit/<int:product_id>/', views.seller_edit_product, name='seller_edit_product'),
    path('sell/delete/<int:product_id>/', views.seller_delete_product, name='seller_delete_product'),

    # User Settings
    path('settings/', views.user_settings, name='user_settings'),

    # Interactive SQL Console & Database Explorer
    path('sql-console/', views.sql_console, name='sql_console'),
]

