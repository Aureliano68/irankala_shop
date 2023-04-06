from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(StoreRoom)
class StoreroomAdmin(admin.ModelAdmin):
    list_display=['product','price','qty','storeroom_type','register']



@admin.register(StoreroomType)
class StoreroomTypeAdmin(admin.ModelAdmin):
    list_display=['storeroom_type_title']
