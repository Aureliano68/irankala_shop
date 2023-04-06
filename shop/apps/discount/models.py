from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from apps.product.models import Product
# Create your models here.
# =========================================================================================
class Cupon(models.Model):
    cupon_code=models.CharField(max_length=10,unique=True,verbose_name='کد کوپن')
    start_date=models.DateTimeField(verbose_name='تاریخ شروع')
    end_date=models.DateTimeField(verbose_name='تاریخ پایان')
    discount=models.IntegerField(verbose_name='درصد تخفیف',validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_active=models.BooleanField(default=False,verbose_name='وضعیت')

    def __str__(self) :
        return self.cupon_code
    
    class Meta:
        db_table = 'cupon'
        managed = True
        verbose_name = 'کوپن تخفیف'
        verbose_name_plural = 'کوپن ها'
    
    
# =========================================================================================
class CuponBasket(models.Model):
    discount_title=models.CharField(max_length=100,verbose_name='عنوان سبد تخفیف')
    start_date=models.DateTimeField(verbose_name='تاریخ شروع')
    end_date=models.DateTimeField(verbose_name='تاریخ پایان')
    discount=models.IntegerField(verbose_name='درصد تخفیف',validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_active=models.BooleanField(default=False,verbose_name='وضعیت')
    
    def __str__(self) :
        return self.discount_title
    
    class Meta:
        db_table = 'cuponbasket'
        managed = True
        verbose_name = 'سبد تخفیف'
        verbose_name_plural = 'سبد های تخفیف'
        
        
# =========================================================================================
class CuponBasketDetail(models.Model):
    cupon_basket=models.ForeignKey(CuponBasket,on_delete=models.CASCADE,verbose_name='سبد تخفیف',related_name='cuponbasketdetail1')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='کالا ',related_name='cuponbasketdetail2')
    
    class Meta:
        db_table = 'cuponbasketdetail'
        managed = True
        verbose_name = '  جزییات سبد تخفیف'
        verbose_name_plural = '  جزییات سبد های تخفیف '
        
# =========================================================================================
