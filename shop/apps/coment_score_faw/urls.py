from django.urls import path
from .views import *
app_name='csf'

urlpatterns = [
    path('create_comment/<slug:slug>',commentView.as_view(),name='create_comment'),
    path('add_score/',add_score,name='add_score')
    
]
