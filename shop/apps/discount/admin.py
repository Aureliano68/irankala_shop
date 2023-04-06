from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display=('cupon_code','start_date','end_date','discount','is_active')
    ordering=('cupon_code',)
    

class Cuponbasketdetailinline(admin.TabularInline):
    model=CuponBasketDetail
    extra=5

@admin.register(CuponBasket)
class CuponBasketAdmin(admin.ModelAdmin):
    list_display=('discount_title','start_date','end_date','discount','is_active')
    ordering=('discount_title',)
    inlines=[Cuponbasketdetailinline,]
    
 