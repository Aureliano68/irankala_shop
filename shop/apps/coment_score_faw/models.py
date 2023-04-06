from django.db import models
from apps.product.models import Product
from apps.account.models import CustomerUser
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
# ==================================================================================
class comment(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_comment',verbose_name='کالا')
    comment_user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name='customer_comment',verbose_name='کاربر نظر دهنده')
    approve_user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name='customer_comment2',verbose_name='کاربر  تایید کننده',null=True,blank=True)
    comment_text=models.TextField(verbose_name="متن نظر")
    register=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ درج')
    is_active=models.BooleanField(default=False,verbose_name='وضعیت')
    comment_parent=models.ForeignKey('comment',on_delete=models.CASCADE,null=True,blank=True,verbose_name='والد نظر',related_name='comment_child')
    
    def __str__(self) :
        return f"{self.product}{self.comment_user}"
    
    class Meta:
        db_table = 'comment'
        managed = True
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        
# ==================================================================================
class Score(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_score',verbose_name='کالا')
    scoring_user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name='customer_score',verbose_name='کاربر نظر دهنده')
    register=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ درج')
    score=models.PositiveIntegerField(verbose_name='امتیاز',validators=[MinValueValidator(0),MaxValueValidator(5)])
    
    def __str__(self) :
        return f"{self.product}{self.score}"
    
    class Meta:
        db_table = 'score'
        managed = True
        verbose_name = 'امتیاز'
        verbose_name_plural = 'امتیازات'
