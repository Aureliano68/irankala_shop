from django.db import models
from apps.account.models import Customer
from apps.product.models import Product
from django.utils import timezone
import uuid
from utilis import price_by_delivery_tax

# Create your models here.
class payment(models.Model):
    payment_title=models.CharField(max_length=50,verbose_name='روش پرداخت')
    
    def __str__(self):
        return self.payment_title
    
    class Meta:
        db_table = 'payment'
        managed = True
        verbose_name = 'روش پرداخت'
        verbose_name_plural = 'روش های پرداخت'
# ====================================================================================================================
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name='مشتری',related_name='orders')
    register_date=models.DateField(default=timezone.now(),verbose_name='تاریخ درج سفارش')
    update_date=models.DateField(auto_now=True,verbose_name=' تاریخ ویرایش سفارش')
    is_finaly=models.BooleanField(default=False,verbose_name="نهایی شده")
    order_code=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,verbose_name='کد تولید شده برای سفارش')
    discount=models.IntegerField(blank=True,null=True,default=0,verbose_name='تخفیف روی فاکتور')
    description=models.TextField(blank=True,null=True,verbose_name='توضیحات')
    payment=models.ForeignKey(payment,on_delete=models.CASCADE,related_name='payment',verbose_name='روش پرداخت',default=1,blank=True,null=True)
    
    def __str__(self):
        return f'{self.customer}\t{self.id}\t{self.is_finaly}'
    
    
    def get_order_total_price(self):
        sum=0
        for item in self.order_detail1.all():
            sum+=item.product.get_price_by_discount()*item.qty
        
        order_final_price,delivery,tax=price_by_delivery_tax(sum,self.discount)
        return int(order_final_price*10)
    
    class Meta:
        db_table = 'order'
        managed = True
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
        
# ====================================================================================================================
class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_detail1',verbose_name='سفارش')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_detail2',verbose_name='کالا')
    qty=models.PositiveIntegerField(default=1,verbose_name='تعداد')
    price=models.IntegerField(verbose_name="قیمت کالا در فاکتور")
    
    def __str__(self):
        return f'{self.order}\t{self.product}\t{self.qty}'
    
    class Meta:
        db_table = 'orderdetail'
        
# ====================================================================================================================

        
    