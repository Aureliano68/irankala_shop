from django.urls import path
from .views import *
app_name='orders'

urlpatterns = [
    path('shop_cart/',shopcartView.as_view(),name='shop_cart'),
    path('show_shop_cart/',show_shopcart,name='show_shop_cart'),
    path('add_to_shop/',add_to_shop,name='add_to_shop'),
    path('delete_from_shop/',delete_from_shop,name='delete_from_shop'),
    path('update_shop_cart/',update_shop_cart,name='update_shop_cart'),
    path('status_of_shop_cart/',status_of_shop_cart,name='status_of_shop_cart'),
    path('create_order/',CreateOrderView.as_view(),name='create_order'),
    path('checkout_order/<int:order_id>',checkoutView.as_view(),name='checkout_order'),





]
