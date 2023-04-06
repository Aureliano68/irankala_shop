from django.contrib import admin
from .models import *
# Register your models here.

class OrderDetailinline(admin.TabularInline):
    model=OrderDetail
    extra=3

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['customer','register_date','is_finaly','discount']
    ordering=['customer']
    inlines=[OrderDetailinline]