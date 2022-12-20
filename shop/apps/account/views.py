from django.shortcuts import render,redirect
from .form import *
from django.views import View
import utilis 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
# ----------------------------------------------------------------------------------------------------------------------------------
class RegisterUserView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterUserForm()
        return render(request,'account/Register.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            active_code=utilis.create_random_code(5)
            CustomerUser.objects.create_user(
                mobile_number=data['mobile_number'],
                active_code=active_code,
                password=data['password1'],
            )
            utilis.send_sms(data['mobile_number'],f'کد فعال سازی حساب شما{active_code}میباشد')
            request.session['user.session']={
                'mobile_number':data['mobile_number'],
                'active_code':str(active_code),
                'remember_change':False

            }
            messages.success(request,' اطلاعات شما ثبت شد.کد فعال سازی را وارد کنید','success')
            return redirect('account:verify')
        messages.error(request,'اطلاعات وارد شده معتبر نمیباشد','danger')
        return redirect('account:register')
    
    
# ----------------------------------------------------------------------------------------------------------------------------------  
class VerifyUserView(View):
     def get(self,request,*args,**kwargs):
        form=VerifyUserForm()
        return render(request,'account/Verify.html',{'form':form})
    
     def post(self,request,*args,**kwargs):
        form=VerifyUserForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user_session= request.session['user_session']
            if data['active_code']==user_session['active_code']:
                user=CustomerUser.objects.get(mobile_number=user_session['mobile_number'])
                if user_session['remember_change']==False:
                    user.is_active==True
                    user.active_code=utilis.create_random_code(5)
                    user.save()
                    messages.success(request,'ثبت نام با موفقیت انجام شد','success')
                    return redirect('main:index')
                else:
                    return redirect('account:changepassword')

            messages.error(request,'کد وارد شده معتبر نمیباشد','danger')
            return redirect('account:verify')
        messages.error(request,'اطلاعات وارد شده معتبر نمیباشد','danger')
        return redirect('account:verify')

# ----------------------------------------------------------------------------------------------------------------------------------
class LoginUserView(View):
    template_name='account/login.html'

    def get(self,request,*args,**kwargs):
        form=LoginUserForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=LoginUserForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(username=data['mobile_number'],password=data['password'])
            if user is not None:
                db_user=CustomerUser.objects.get(mobile_number=data['mobile_number'])
                if db_user.is_admin==False:
                    messages.success(request,' ورود با موفقیت انجام شد','success')
                    login(request,user)
                    next_url=request.GET.get('next')
                    if next_url is not None:
                        return redirect(next_url)
                    else:
                        return redirect('main:index')
                else:
                        messages.warning(request,' ادمین نمیتواند از اینجا وارد شود','warning')
                        return render(request,self.template_name,{'form':form})              
            else:
                messages.error(request,'اطلاعات وارد شده کسشر است','danger')
                return render(request,self.template_name,{'form':form})
        messages.error(request,'اطلاعات وارد شده معتبر نمیباشد','danger')
        return render(request,self.template_name,{'form':form})
                    
# ----------------------------------------------------------------------------------------------------------------------------------
class LogoutUser(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('main:index')                

# ----------------------------------------------------------------------------------------------------------------------------------
class ChangePasswordUserView(View):
    template_name='account/changepassworduser.html'

    def get(self,request,*args,**kwargs):
        form=changePasswordUserForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=changePasswordUserForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user_session=request.session['user_session']
            user=CustomerUser.objects.get(mobile_number=user_session['mobile_number'])
            user.set_password(data['password1'])
            user.active_code=utilis.create_random_code(5)
            user.save()
            messages.success(request,'تغییر رمز شما با موفقیت انجام شد','success')
            return redirect('account:login')
        
        messages.error(request,'اطلاعات وارد شده معتبر نمیباشد','danger')
        return render(request,self.template_name,{'form':form})

            

# ----------------------------------------------------------------------------------------------------------------------------------
class RememberchangeView(View):
    template_name='account/Remember.html'

    def get(self,request,*args,**kwargs):
        form=RememberForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=RememberForm(request.POST)
        if form.is_valid():
            try:
                data=form.cleaned_data
                user=CustomerUser.objects.get(mobile_number=data['mobile_number'])
                active_code=utilis.create_random_code(5)
                user.active_code=active_code
                user.save()
                utilis.send_sms(data['mobile_number'],f'کد فعال سازی حساب شما{active_code}میباشد')
                request.session['user_session']={
                        'mobile_number':data['mobile_number'],
                        'active_code':str(active_code),
                        'remember_change':True
                    }
                messages.success(request,'  کد ارسالی را وارد کنید   ','success')
                return redirect('account:verify')
            except:
                 messages.error(request,'شماره موبایل وارد شده اشتباه است','danger')
                 return render(request,self.template_name,{'form':form})
           
        messages.error(request,'اطلاعات وارد شده نا معتبر است','danger')
        return render(request,self.template_name,{'form':form})
                

            
