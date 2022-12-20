from django.urls import path
from .views import *
app_name='account'
urlpatterns = [
    path('register/',RegisterUserView.as_view(),name='register'),
    path('verify/',VerifyUserView.as_view(),name='verify'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('changepassword/',ChangePasswordUserView.as_view(),name='changepassword'),
    path('Remember/',RememberchangeView.as_view(),name='Remember'),




]
