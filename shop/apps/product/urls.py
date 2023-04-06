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
    # path('ajax_admin/',get_filter_value_for_feature,name='ajax_admin'),
    path('productgroup_filter/',Get_productgrups_for_filter,name='productgroup_filter'),
    path('brand_filter/<slug:slug>',get_branf_for_filter,name='brand_filter'),
    path('feature_filter/<slug:slug>',feature_value_for_filter,name='feature_filter'),









    
]
