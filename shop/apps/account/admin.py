from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import *

class CustomerUserAdmin(UserAdmin):
        form = UserChangeForm
        add_form = UserCreateForm
        
        list_display=('mobile_number','email','name','family','gender','is_active','is_admin')
        list_filter=['is_active','is_admin']
        search_fields = ("name", "mobile_number")
        ordering = ("mobile_number",)
        
        fieldsets = (
        (None, {"fields": ("mobile_number", "password")}),
        (("Personal info"), {"fields": ("name", "family", "gender","email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    'is_admin',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                   
                ),
            },
        ),
       
        )
        add_fieldsets = (
            (None, {"fields": ('mobile_number','email','name','family','gender','password1','password2')}),
        )

        filter_horizontal = (
           "groups",
           "user_permissions",)
        
        
admin.site.register(CustomerUser,CustomerUserAdmin)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','phone']