from django.contrib import admin
from .models import comment
# Register your models here.

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display=['product','comment_user','comment_text','is_active']
    list_editable=['is_active']
