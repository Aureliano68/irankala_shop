from django.urls import path
from .views import *
app_name='product'
urlpatterns = [
    path('cheap_product/',cheap_product,name='cheap_product'),
    path('last_product/',last_product,name='last_product'),
    path('like_product_group/',like_product_group,name='like_product_group'),
    path('Detail_Product/<slug:slug>/',Detail_Product.as_view(),name='Detail_Product'),
    path('relate_product/<slug:slug>/',relate_product,name='relate_product'),
    path('get_group_product/<slug:slug>/',get_product.as_view(),name='get_group_product'),
    path('productlistgroup/',productlistgroup.as_view(),name='productlistgroup'),





    
]
