from django.db import models
from apps.orders.models import Order
from apps.account.models import Customer
from django.utils import timezone
# Create your models here.


class Payment(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='payment_order',verbose_name='سفارش')
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='payment_customer',verbose_name='مشتری')
    register=models.DateTimeField(default=timezone.now,verbose_name='تاریخ پرداخت')
    update_date=models.DateTimeField(auto_now=True,verbose_name='تاریخ ویرایش پرداخت')
    amount=models.IntegerField(verbose_name='مبلغ پرداخت')
    discription=models.TextField(verbose_name='توضیحات پرداخت')
    is_finaly=models.BooleanField(default=False,verbose_name='وضعیت پرداخت')
    status_code=models.IntegerField(verbose_name='کد وضعیت درگاه پرداخت',null=True,blank=True)
    rf_id=models.CharField(max_length=50,verbose_name='شماره پیگیری پرداخت',null=True,blank=True)
    
    def __str__(self) :
        return f'{self.order} {self.customer} {self.rf_id}'
    
    class Meta:
        managed = True
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت ها'

    