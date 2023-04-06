from django.db import models
from apps.account.models import CustomerUser
from apps.product.models import Product

# Create your models here.
# ================================================================================
class StoreroomType(models.Model):
    storeroom_type_title=models.CharField(max_length=50,verbose_name='نوع انبار')
    
    def __str__(self) :
        return self.storeroom_type_title
    
    class Meta:
        db_table = 'storeroomtype'
        managed = True
        verbose_name = 'نوع انبار'
        verbose_name_plural = 'انبار روش انبار'

# ================================================================================
class StoreRoom(models.Model):
    storeroom_type=models.ForeignKey(StoreroomType,on_delete=models.CASCADE,related_name='storerooms',verbose_name='انبار')
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name='storeroom_users',verbose_name='کاربر')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='storeroom_products',verbose_name='کالا')
    qty=models.PositiveIntegerField(verbose_name='تعداد')
    price=models.PositiveIntegerField(verbose_name='قیمت',null=True,blank=True)
    register=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت')
    
    def __str__(self) :
        return f"{self.storeroom_type}{self.product}"
    
    class Meta:
        db_table = 'storeroom'
        managed = True
        verbose_name = ' انبار'
        verbose_name_plural = 'انبارها'
        
# ================================================================================
