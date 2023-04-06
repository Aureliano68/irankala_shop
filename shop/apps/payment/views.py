from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from apps.orders.models import Order
from django.http import HttpResponse
import requests
import json
from django.core.exceptions import ObjectDoesNotExist
from .models import Payment
from apps.account.models import Customer
from apps.storeroom.models import StoreRoom,StoreroomType


# Create your views here.
MERCHANT = '0C8B70F6-F28B-4E66-8D98-FED8A6229A18'
ZP_API_REQUEST = "https://sandbox.banktest.ir/zarinpal/api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://sandbox.banktest.ir/zarinpal/api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://sandbox.banktest.ir/zarinpal/www.zarinpal.com/pg/StartPay/{authority}"
CallbackURL = 'http://127.0.0.1:8000/payment/verify/'


class ZarinpallPaymentView(LoginRequiredMixin,View):
    def get(self,request,order_id):
        try:
            discription='پرداخت از طریق درگاه زرین پال'     
            order=Order.objects.get(id=order_id)
            payment=Payment.objects.create(
                order=order,
                customer=Customer.objects.get(user=request.user),
                amount=order.get_order_total_price(),
                discription=discription,
                
            )
            payment.save()
            
            request.session['payment_session']={
               'order_id':order.id,
               'payment_id':payment.id
                
            }
            
            user=request.user
            req_data = {
            "merchant_id": MERCHANT,
            "amount": order.get_order_total_price(),
            "callback_url": CallbackURL,
            "description": discription,
            "metadata": {"mobile": user.mobile_number, "email": user.email}
            }
            
            req_header = {"accept": "application/json","content-type": "application/json'"}
            req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)           
            authority = req.json()['data']['authority']
            if len(req.json()['errors']) == 0:
                return redirect(ZP_API_STARTPAY.format(authority=authority))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        except ObjectDoesNotExist:
            return redirect('orders:checkout_order',order_id)

class ZarinpallPaymentVrifyView(LoginRequiredMixin,View):
    def get(self,request):

        t_status = request.GET.get('Status')
        t_authority = request.GET['Authority']
        if request.GET.get('Status') == 'OK':
            order_id=request.session['payment_session']['order_id']
            payment_id=request.session['payment_session']['payment_id']
            order=Order.objects.get(id=order_id)
            payment=Payment.objects.get(id=payment_id)
            req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
            req_data = {
                "merchant_id": MERCHANT,
                "amount":  order.get_order_total_price(),
                "authority": t_authority
                    }
            req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
            if len(req.json()['errors']) == 0:
                t_status = req.json()['data']['code']
                if t_status == 100:
                    order.is_finaly=True
                    order.save()
                    
                    for item in order.order_detail1.all():
                        StoreRoom.objects.create(
                            storeroom_type=StoreroomType.objects.get(id=2),
                            user=request.user,
                            product=item.product,
                            qty=item.qty,
                            price=item.price
                        )
            
                    payment.is_finaly=True
                    payment.status_code=t_status
                    payment.rf_id=str( req.json()['data']['ref_id'])
                    payment.save()
                    return redirect('payment:show_vreify_message',f"پرداخت با مو فقیت انجام شد و کد رهگیری شما {str( req.json()['data']['ref_id'])}")
                       
                elif t_status == 101:
                    order.is_finaly=True
                    order.save()
                    
                    for item in order.order_detail1.all():
                        StoreRoom.objects.create(
                            storeroom_type=StoreroomType.objects.get(id=2),
                            user=request.user,
                            product=item.product,
                            qty=item.qty,
                            price=item.price
                        )
                    
                  
                    payment.is_finaly=True
                    payment.status_code=t_status
                    payment.rf_id=str( req.json()['data']['ref_id'])
                    payment.save()
                    return redirect('payment:show_vreify_message',f"پرداخت قبلا انجام شده و کد رهگیری شما {str( req.json()['data']['ref_id'])}")
                    
                  
                else:
                    payment.status_code=t_status
                    payment.save()
                    return redirect('payment:show_vreify_message',f"خطا در فرآیند پرداخت و کد وضعیت:{t_status}")


            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return redirect('payment:show_vreify_message',f"خطا در فرآیند پرداخت و کد خطا: Error code: {e_code}, Error Message: {e_message}")

        else:
            return redirect('payment:show_vreify_message',f"خطا در فرآیند پرداخت ")





def show_vreify_messsage(request,message):
    return render(request,'payment/message_vreify.html',{'message':message})