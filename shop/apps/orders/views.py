from django.shortcuts import render,get_object_or_404,redirect
from .shop_cart import shopcart
from django.views import View
from apps.product.models import Product
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.account.models import Customer
from .models import Order,OrderDetail,payment
from .forms import OrderForm
from django.core.exceptions import ObjectDoesNotExist
from .forms import OrderForm
from django.contrib import messages
from utilis import price_by_delivery_tax
# Create your views here.
# ===========================================================================================
class shopcartView(View):
    def get(self,request,*args,**kwargs):
        shop_cart=shopcart(request)
        return render(request,'orders/shop_cart.html',{'shop_cart':shop_cart})
    
# ===========================================================================================
def show_shopcart(request):
    shop_cart=shopcart(request)
    total_price=shop_cart.clac_total_price()
    order_final_price,delivery,tax=price_by_delivery_tax(total_price)
    context={
        'shop_cart':shop_cart,
        'shopcart_count':shop_cart.count,
        'total_price':total_price,
        'delivery':delivery,
        'tax':int(tax),
        'order_final_price':order_final_price
    }
    return render(request,'orders/partials/show_shop_cart.html',context)

# ===========================================================================================       
def add_to_shop(request):
    product_id=request.GET.get('product_id')
    qty=request.GET.get('qty')
    shop_cart=shopcart(request)
    product=get_object_or_404(Product,id=product_id)
    shop_cart.add_to_shop_cart(product,qty)
    return HttpResponse(shop_cart.count)

# ===========================================================================================
def delete_from_shop(request):
    product_id=request.GET.get('product_id')
    product=get_object_or_404(Product,id=product_id)
    shop_cart=shopcart(request)
    shop_cart.delete_from_shop_cart(product)
    return redirect('orders:show_shop_cart')

# ===========================================================================================
def update_shop_cart(request):
    product_id_list=request.GET.getlist('product_id_list[]')
    qty_list=request.GET.getlist('qty_list[]')
    shop_cart=shopcart(request)
    shop_cart.update( product_id_list,qty_list)
    return redirect('orders:show_shop_cart')

# ===========================================================================================
def status_of_shop_cart(request):
    shop_cart=shopcart(request)
    return HttpResponse(shop_cart.count)

# ===========================================================================================
class CreateOrderView(LoginRequiredMixin,View):
    def get(self,request):
        try:
            customer=Customer.objects.get(user=request.user)
        except ObjectDoesNotExist:
             customer=Customer.objects.create(user=request.user)
       
        order=Order.objects.create(customer=customer)
        shop_cart=shopcart(request)
        for item in shop_cart:
            OrderDetail.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                qty=item['qty']
                
            )

        return redirect('orders:checkout_order',order.id)

# ===========================================================================================
class checkoutView(LoginRequiredMixin,View):
    def get(self,request,order_id):
        user=request.user
        customer=get_object_or_404(Customer,user=user)
        shop_cart=shopcart(request)
        order=get_object_or_404(Order,id=order_id)
        total_price=shop_cart.clac_total_price()
        order_final_price,delivery,tax=price_by_delivery_tax(total_price,order.discount)
        data={
            'name':user.name,
            'family':user.family,
            'email':user.email,
            'phone':customer.phone,
            'address':customer.address,
            'phone':customer.phone,
            'description':order.description,
            'payment':order.payment

            

        }
        form=OrderForm(data)
        context={
            'shop_cart':shop_cart,
            'total_price':total_price,
            'delivery':delivery,
            'tax':int(tax),
            'order_final_price':int(order_final_price),
            'order':order,
            'form':form
        }
        return render(request,'orders/cheakout.html',context)
        
    def post(self,request,order_id):   
        form=OrderForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            try:   
                order=Order.objects.get(id=order_id)
                order.description=data['description']
                order.payment=payment.objects.get(id=data['payment_type'])
                order.save()
                
                user=request.user
                user.name=data['name']
                user.family=data['family']
                user.email=data['email']
                user.save()
                
                customer=Customer.objects.get(user=user)
                customer.phone=data['phone']
                customer.address=data['address']
                customer.save()

                messages.success(request,'اطلاعات با موفقیت ثبت شد','success')
                return redirect('payment:zarnpal_payment',order.id)
                
            except ObjectDoesNotExist :
                messages.error(request,'فاکتوری با این مشخصات یافت نشد','danger')
                return redirect('orders:checkout_order',order.id)
        return redirect('orders:checkout_order',order.id)


        

        
    

        
        