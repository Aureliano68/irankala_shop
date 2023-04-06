from django.urls import path
from .views import *

app_name='payment'
urlpatterns = [
    path('zarnpal_payment/<int:order_id>/',ZarinpallPaymentView.as_view(),name='zarnpal_payment'),
    path('verify/',ZarinpallPaymentVrifyView.as_view(),name='verify'),
    path('show_vreify_message/<str:message>/',show_vreify_messsage,name='show_vreify_message')


]
