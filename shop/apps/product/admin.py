from django.contrib import admin
from .models import *
from django.db.models.aggregates import Count
from admin_decorators import short_description,order_field
from django.http import HttpResponse
from django.core import serializers
from django_admin_listfilter_dropdown.filters import ( DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter )
from django.db.models import Q
from django.contrib.admin import SimpleListFilter


# Register your models here.
# =================================================================================================================================
@short_description('غیر فعال کردن گروه کالا')
def de_active_product_group(modeladmin,request,queryset):
    res=queryset.update(is_active=False)
    message=f'تعداد{res}گروه کالا غیر فعال شد'
    modeladmin.message_user(request,message)

# -------------------------------------------------------------------------------   
@short_description(' فعال کردن گروه کالا')
def active_product_group(modeladmin,request,queryset):
    res=queryset.update(is_active=True)
    message=f'تعداد {res} گروه کالا غیر فعال شد'
    modeladmin.message_user(request,message)
    
# ------------------------------------------------------------------------------- 
@short_description('گرفتن خروجی جیسون از گروه کالاها')
def export_json_product_group(modeladmin,request,queryset):
    response=HttpResponse(content_type='application/json')
    serializers.serialize('json',queryset,stream=response)
    return response

# ------------------------------------------------------------------------------- 
class GroupFilter(SimpleListFilter):
    title='گروه محصولات'
    parameter_name='group'
    
    def lookups(self, request, model_admin):
        sub_group=GroupProduct.objects.filter(~Q(group_parent=None))
        groups=set([ item.group_parent for item in sub_group])
        return [(item.id,item.grouppro_name) for item in groups ]
    
    def queryset(self, request, queryset):   
        if self.value()!=None: 
            return queryset.filter(Q(group_parent=self.value()))
        return queryset


# -------------------------------------------------------------------------------   
class ProductGroupinstanceInline(admin.TabularInline):
    model=GroupProduct 
    extra=3

@admin.register(GroupProduct)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display=('grouppro_name','is_active','register_date','publish_date','group_parent','count_sub_group','count_sub_pro')
    list_filter=(GroupFilter,)
    search_fields=('grouppro_name',)
    ordering=('group_parent',)
    inlines=[ProductGroupinstanceInline]
    actions=[de_active_product_group,active_product_group,export_json_product_group]
    list_editable=('is_active',)
# -------------------------------------------------------------------------------   
    def get_queryset(self,*args,**kwargs):
        queryset = super(ProductGroupAdmin, self).get_queryset(*args,**kwargs)
        queryset = queryset.annotate(sub_group=Count('groups'))
        queryset = queryset.annotate(sub_pro=Count('product_of_group'))
        return queryset
    
    @short_description('تعداد زیر گروه ')
    def count_sub_group(self,obj):
        return obj.sub_group
       
    @short_description('تعداد  کالا ')
    def count_sub_pro(self,obj):
        return obj.sub_pro    
    
# =================================================================================================================================
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=('brand_name','slug')
    list_filter=('brand_name',)
    search_fields=('brand_name',)
    
# =================================================================================================================================
@admin.register(Feature)
class featureAdmin(admin.ModelAdmin):
    list_display=('feature_name',)
    list_filte=('feature_name',)
    search_fields=('feature_name',)
    ordering=('feature_name',)

# =================================================================================================================================
@short_description('غیر فعال کردن گروه کالا')
def de_active_product(modeladmin,request,queryset):
    res=queryset.update(is_active=False)
    message=f'تعداد{res} کالا غیر فعال شد'
    modeladmin.message_user(request,message)

# -------------------------------------------------------------------------------   
@short_description(' فعال کردن گروه کالا')
def active_product(modeladmin,request,queryset):
    res=queryset.update(is_active=True)
    message=f'تعداد {res}  کالا غیر فعال شد'
    modeladmin.message_user(request,message)
    
# ------------------------------------------------------------------------------- 
@short_description('گرفتن خروجی جیسون از  کالاها')
def export_json_product(modeladmin,request,queryset):
    response=HttpResponse(content_type='application/json')
    serializers.serialize('json',queryset,stream=response)
    return response

# -------------------------------------------------------------------------------  
class ProductinstanceInline(admin.TabularInline):
    model=ProductFeature 
    extra=3
    
# -------------------------------------------------------------------------------    
class GaleryProductinstanceInline(admin.TabularInline):
    model=GaleryProduct 
    extra=3
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','is_active','price','product_description','brand','register_date','publish_date','display_product_group')
    list_filter=("product_name",)
    search_fields=('product_name',)
    inlines=[ProductinstanceInline,GaleryProductinstanceInline]
    actions=[de_active_product,active_product,export_json_product]
    
    
    @short_description('گروه کالا')
    def display_product_group(self,obj):
        return [group.grouppro_name for group in obj.group_pro.all()]
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name=='group_pro':
            kwargs['queryset']=GroupProduct.objects.filter(~Q(group_parent=None))
        return super().formfield_for_manytomany(db_field, request, **kwargs)
            
    fieldsets = (
        ('اطلاعات کالا', {
            "fields": (
            ('product_name','price','product_image','slug'),
            'is_active',
            ('product_description','full_description'),
            ('group_pro','brand')
            ),
        }),
        ('تاریخ و زمان',{"fields":("publish_date",)})
    )
    
# =================================================================================================================================
