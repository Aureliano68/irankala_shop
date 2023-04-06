from django.shortcuts import render,get_object_or_404
from .models import *
from django.views import View
from django.db.models import Q,Count
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Max, Min


# Create your views here.
# ------------------------------------------------------------------------------- 
def get_group_product():
    return GroupProduct.objects.filter(Q(is_active=True) & Q(group_parent=None))

# ------------------------------------------------------------------------------- 
def cheap_product(request,*args,**kwargs):
    products=Product.objects.filter(is_active=True ).order_by('price')[:7]
    group_product=get_group_product()
    context={
        'products':products,
        'group_product':group_product
    }
    return render(request,'product/partial/cheap_product.html',context)

# ------------------------------------------------------------------------------- 
def last_product(request,*args,**kwargs):
    products=Product.objects.filter(is_active=True).order_by('publish_date')[:8]
    group_product=get_group_product()
    context={
        'products':products,
        'group_product':group_product
    }
    return render(request,'product/partial/last_product.html',context)

# ------------------------------------------------------------------------------- 
def like_product_group(request,*args,**kwargs):
    product_group=GroupProduct.objects.filter(Q(is_active=True)).annotate(count=Count('product_of_group')).order_by('-count')[:6]
    context={
        'group_product':product_group
    }
    return render(request,'product/partial/like_product.html',context)


# =================================================================================================================================
class Detail_Product(View):
    def get(self,request,slug):
        product=get_object_or_404(Product,slug=slug)
        if product.is_active==True:
            return render(request,'product/partial/Detail_Product.html',{'product':product})
        
# =================================================================================================================================
def relate_product(request,*args,**kwargs):
    curent_product=get_object_or_404(Product,slug=kwargs['slug'])
    relate_product=[]
    for item in curent_product.group_pro.all():
        relate_product.extend(Product.objects.filter(Q(is_active=True) & Q(group_pro=item) & ~Q(id=curent_product.id)))
    return render(request,'product/partial/relate_product.html',{'relate_product':relate_product})
        
# =================================================================================================================================
class productlistgroup(View):
    def get(self,request,*args,**kwargs):
        group_product=GroupProduct.objects.filter(Q(is_active=True)).annotate(count=Count('product_of_group')).order_by('-count')
        return render(request,'product/partial/product_group_all.html',{'group_product':group_product})
    
# =================================================================================================================================
class get_product(View):
     def get(self,request,slug):
        Group_product=get_object_or_404(GroupProduct,slug=slug)
        products=Product.objects.filter(Q(is_active=True) & Q(group_pro=Group_product))   
        
        res_aggre=products.aggregate(min=Min('price'),max=Max('price')) 
    # branf filter
        brand_filter=request.GET.getlist('brand')
        if brand_filter:
            products=products.filter(brand__id__in=brand_filter)
       
    # branf feature
        feature_filter=request.GET.getlist('feature')
        if feature_filter:
            products=products.filter(feature_pro__filter_value__id__in=feature_filter).distinct()
            
        
        group_slug=slug
        product_per_page=2
        paginator=Paginator(products,product_per_page)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        product_count=products.count()

        context={
            'product':products,
            'Group_product':Group_product,
            'group_slug':group_slug,
            'page_obj':page_obj,
            'product_count':product_count,
            'res_aggre':res_aggre
            
        }
        return render(request,'product/partial/get_Product.html',context)
    

# =================================================================================================================================
# def get_filter_value_for_feature(request):
#     if request.method=="GET":
#         feature_id=request.GET["feature_id"]
#         feature_value=FeatureValue.objects.filter(feature_id=feature_id)
#         res={ fv.value_title:fv.id   for fv in feature_value}
#         return JsonResponse(data=res , safe=False)

# =================================================================================================================================
# لیست گروه محصولات برای فیلتر
def Get_productgrups_for_filter(request):
    groupproduct=GroupProduct.objects.annotate(count=Count('product_of_group')).filter(Q(is_active=True) & ~Q(count=0)).order_by('-count')
    return render(request,'product/partial/productgroup_for_filter.html',{'groupproduct':groupproduct})
     
# =================================================================================================================================
# لیست برند ها برای فیلتر

def get_branf_for_filter(request,*args,**kwargs):
    group_products=get_object_or_404(GroupProduct,slug=kwargs['slug'])
    brand_list_id=group_products.product_of_group.filter(is_active=True).values('brand_id')
    brand=Brand.objects.filter(pk__in=brand_list_id).annotate(count=Count('brands')).filter(~Q(count=0)).order_by('-count')
    return render(request,'product/partial/brand_filter.html',{'brandss':brand})

# =================================================================================================================================
# لیست ویزگی ها برای فیلتر
def feature_value_for_filter(request,*args,**kwargs):
    group_products=get_object_or_404(GroupProduct,slug=kwargs['slug'])
    feature_list=group_products.feature_of_group.all()
    feature_dict=dict()
    for feature in feature_list:
        feature_dict[feature]=feature.product_feature_value.all()
    return render(request,'product/partial/feature_filter.html',{'feature_dict':feature_dict})

        
# =================================================================================================================================
