"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.main.urls',namespace='main'),name='main'),
    path('accounts/',include('apps.account.urls',namespace='accounts'),name='accounts'),
    path('product/',include('apps.product.urls',namespace='product'),name='product'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('orders/',include('apps.orders.urls',namespace='orders'),name='orders'),
    path('discount/',include('apps.discount.urls',namespace='discount'),name='discount'),
    path('payment/',include('apps.payment.urls',namespace='payment'),name='payment'),
    path('storeroom/',include('apps.storeroom.urls',namespace='storeroom'),name='storeroom'),
    path('csf/',include('apps.coment_score_faw.urls',namespace='csf'),name='csf'),







    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
