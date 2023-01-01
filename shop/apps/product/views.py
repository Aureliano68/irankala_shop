from django.shortcuts import render,get_object_or_404
from .models import *
from django.views import View
from django.db.models import Q,Count
# Create your views here.
# ------------------------------------------------------------------------------- 
def get_group_product():
    return GroupProduct.objects.filter(Q(is_active=True) & Q(group_parent=None))

# ------------------------------------------------------------------------------- 
def cheap_product(request,*args,**kwargs):
    products=Product.objects.filter(is_active=True ).order_by('price')[:5]
    group_product=get_group_product()
    context={
        'products':products,
        'group_product':group_product
    }
    return render(request,'product/partial/cheap_product.html',context)

# ------------------------------------------------------------------------------- 
def last_product(request,*args,**kwargs):
    products=Product.objects.filter(is_active=True).order_by('publish_date')[:4]
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
class get_product(View):
     def get(self,request,slug):
        Group_product=get_object_or_404(GroupProduct,slug=slug)
        products=Product.objects.filter(Q(is_active=True) & Q(group_pro=Group_product))
        return render(request,'product/partial/get_Product.html',{'product':products,'Group_product':Group_product})
    
# =================================================================================================================================
class productlistgroup(View):
    def get(self,request,*args,**kwargs):
        group_product=GroupProduct.objects.filter(Q(is_active=True)).annotate(count=Count('product_of_group')).order_by('-count')
        return render(request,'product/partial/product_group_all.html',{'group_product':group_product})



    