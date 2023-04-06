from django.db import models
from utilis import FileUpload
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField 
from django.urls import reverse
from datetime import datetime
from django.db.models import Sum,Avg
import middlewares 
# Create your models here.
# =================================================================================================================================
class GroupProduct(models.Model):
    grouppro_name=models.CharField(max_length=50,verbose_name='نام گروه کالا')
    image_upload=FileUpload('images','productgroup')
    grouppro_image=models.ImageField(upload_to=image_upload.imageupload,verbose_name='تصویر گروه کالا')
    grouppro_description=models.TextField(null=True,blank=True,verbose_name='توضیحات')
    is_active=models.BooleanField(default=True,verbose_name='وضعیت فعال/غیر فعال')
    register_date=models.DateTimeField(auto_now_add=True,verbose_name=' تاریخ درج')
    publish_date=models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    update=models.DateTimeField(auto_now=True,verbose_name=' تاریخ اخرین بروزرسانی')
    slug=models.SlugField(max_length=100,null=True)
    group_parent=models.ForeignKey('GroupProduct',on_delete=models.CASCADE,verbose_name='والد گروه کالا',null=True,blank=True,related_name='groups')
    
    def __str__(self):
        return f'{self.grouppro_name}'
    class Meta:
        db_table = 'groupproduct'
        managed = True
        verbose_name = 'گروه کالا'
        verbose_name_plural = 'گروه های کالاها'
        

# =================================================================================================================================
class Brand(models.Model):
    brand_name=models.CharField(max_length=50,verbose_name='نام برند')
    image_upload=FileUpload('images','brand')
    brand_image=models.ImageField(upload_to=image_upload.imageupload,verbose_name='تصویر برند')
    slug=models.SlugField(max_length=100,null=True)

    def __str__(self):
        return f'{self.brand_name}'
    
    class Meta:
        db_table = 'brand'
        managed = True 
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'
        
        
# =================================================================================================================================
class Feature(models.Model):
    feature_name=models.CharField(max_length=50,verbose_name='نام ویژگی')
    group_PRODUCT=models.ManyToManyField(GroupProduct,verbose_name='گروه کالا',related_name='feature_of_group')
    
    def __str__(self):
        return f'{self.feature_name}'
    
    class Meta:
        db_table = 'feature'
        managed = True
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'
        
        
# =================================================================================================================================
class Product(models.Model):
    product_name=models.CharField(max_length=50,verbose_name='نام کالا')
    price=models.PositiveIntegerField(default=0,verbose_name="قیمت کالا")
    image_upload=FileUpload('images','product')
    product_image=models.ImageField(upload_to=image_upload.imageupload,verbose_name='تصویر  کالا')
    product_description=RichTextUploadingField(blank=True,null=True,config_name='default')
    full_description=models.TextField(blank=True,null=True,default='',verbose_name='توضیحات کامل')
    is_active=models.BooleanField(default=True,verbose_name='وضعیت فعال/غیر فعال')
    register_date=models.DateTimeField(auto_now_add=True,verbose_name=' تاریخ درج')
    publish_date=models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
    update=models.DateTimeField(auto_now=True,verbose_name=' تاریخ اخرین بروزرسانی')
    slug=models.SlugField(max_length=100,null=True)
    group_pro=models.ManyToManyField(GroupProduct,verbose_name='گروه کالا',related_name='product_of_group')
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name='برند کالا',related_name='brands')
    features=models.ManyToManyField(Feature,verbose_name='گروه کالا',through='ProductFeature')

    def __str__(self):
        return f'{self.product_name}'
    
    def get_absolute_url(self):
        return reverse("product:Detail_Product", kwargs={"slug": self.slug})
    
    def get_price_by_discount(self):
        list1=[]
        for item in self.cuponbasketdetail2.all():
            if(
                item.cupon_basket.is_active==True and 
                item.cupon_basket.start_date <= datetime.now() and 
                datetime.now() <= item.cupon_basket.end_date  ):
                list1.append(item.cupon_basket.discount)
        discount=0
        if (len(list1)>0) :
            discount=max(list1)
            
        return self.price-(self.price*discount/100)
    
    
    def get_number_in_storeroom(self):
        sum1=self.storeroom_products.filter(storeroom_type_id=1).aggregate(Sum('qty'))
        sum2=self.storeroom_products.filter(storeroom_type_id=2).aggregate(Sum('qty'))
        input=0
        if sum1['qty__sum']!=None:
            input=sum1['qty__sum']
        
        output=0
        if sum2['qty__sum']!=None:
            output=sum2['qty__sum']
        return input-output
    
    
    # میزان امتیازی که کاربر جاری به این کالا داده
    def get_user_score(self):
        request=middlewares.RequestMiddlewar(get_response=None)
        request=request.thread_local.current_request
        score=0
        user_score=self.customer_score.all().filter(scoring_user=request.user)
        if user_score.count()>0:
            score=user_score[0].score
        return score
        
    
    
    # میانگین امتیازی که این کالا کسب کرده
    def get_avg_score(self):
        avgscore=self.product_score.all().aggregate(Avg('score'))['score__avg']
        if avgscore==None:
            avgscore=0
        return avgscore

    
    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'
        

# =================================================================================================================================
class FeatureValue(models.Model):
    value_title=models.CharField(max_length=100,verbose_name='عنوان مقدار')
    feature=models.ForeignKey(Feature,on_delete=models.CASCADE,null=True,blank=True,verbose_name=' ویژگی',related_name='product_feature_value')
    
    def __str__(self) -> str:
        return f'{self.value_title}'
    
    class Meta:
        db_table = 'featurevalue'
        managed = True
        verbose_name = 'مقدار ویژگی'
        verbose_name_plural = 'مقادیر ویژگی ها'
        
# =================================================================================================================================
class ProductFeature(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=' کالا',related_name='feature_pro')
    feature=models.ForeignKey(Feature,on_delete=models.CASCADE,verbose_name=' ویژگی')
    value=models.CharField(max_length=50,verbose_name='مقدار ویژگی کالا')
    filter_value=models.ForeignKey(FeatureValue,on_delete=models.CASCADE,null=True,blank=True,verbose_name=' مقادیر ویزگی انتخابی',related_name='product_filter_value')
    
    def __str__(self):
        return f'{self.value}'
    
    class Meta:
        db_table = 'productfeature'
        managed = True
        verbose_name = 'ویژگی محصول'
        verbose_name_plural = 'ویژگی محصولات'
        
        
# =================================================================================================================================
class GaleryProduct(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='کالا',related_name='galery_of_product')
    image_upload=FileUpload('images','Galery_product')
    product_image=models.ImageField(upload_to=image_upload.imageupload,verbose_name='تصاویر کالا')
    
    class Meta:
        db_table = 'galeryproduct'
        managed = True
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصولات'
        

# =================================================================================================================================

        
class GaleryProduct(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='کالا',related_name='galery_of_product')
    image_upload=FileUpload('images','Galery_product')
    product_image=models.ImageField(upload_to=image_upload.imageupload,verbose_name='تصاویر کالا')
    
    class Meta:
        db_table = 'galeryproduct'
        managed = True
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصولات'