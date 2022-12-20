from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser,PermissionsMixin,UserManager
# Create your models here.

# ----------------------------------------------------------------------------------------------------------------------------------
class CustomerManager(BaseUserManager):
    def create_user(self,mobile_number,email='',name='',family='',gender=None,active_code=None,password=None):
        if not mobile_number :
            raise ValueError('شماره موبایل الزامی است')
        user=self.model(
            mobile_number=mobile_number,
            email=email,
            name=name,
            family=family,
            gender=gender,
            active_code=active_code
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
# -----------------------------------------------------------------
    def create_superuser(self,mobile_number,email,name,family,gender=None,active_code=None,password=None):
        user=self.create_user(
            mobile_number=mobile_number,
            email=email,
            name=name,
            family=family,
            gender=gender,
            active_code=active_code,
            password=password
        )
        user.is_active=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
        
        
# ----------------------------------------------------------------------------------------------------------------------------------
class CustomerUser(AbstractBaseUser,PermissionsMixin):
    mobile_number=models.CharField(max_length=11,unique=True,verbose_name='شماره موبایل')
    email=models.CharField(max_length=200,blank=True)
    name=models.CharField(max_length=50,blank=True)
    family=models.CharField(max_length=50,blank=True)
    Gender_choice=(('m','male'),('f','female'))
    gender=models.CharField(max_length=50,blank=True,null=True,choices=Gender_choice,default='m')
    regester_date=models.DateField(default=timezone.now())
    is_active=models.BooleanField(default=False)
    active_code=models.CharField(max_length=50,blank=True,null=True)
    is_admin=models.BooleanField(default=False)
    
    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ["email","name","family"]
    
    objects=CustomerManager()
    
    def __str__(self) :
       return f'{self.name}\t{self.family}'
   
    @property
    def is_staff(self):
        return self.is_admin==True

# ----------------------------------------------------------------------------------------------------------------------------------
