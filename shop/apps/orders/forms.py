from django import forms
from .models import payment
class OrderForm(forms.Form):
    name=forms.CharField(label='نام',
                         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام'}),
                         error_messages={'required':'این فیلد نمیتواند خالی باشد'}
                         )
    
    family=forms.CharField(label='نام خانوادگی',
                         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خانوادگی'}),
                         error_messages={'required':'این فیلد نمیتواند خالی باشد'}
                         )
    
    address=forms.CharField(label='آدرس ',
                         widget=forms.Textarea(attrs={'class':'form-control','placeholder':' آدرس','rows':'3'}),
                         error_messages={'required':'این فیلد نمیتواند خالی باشد'}
                         )
    
    email=forms.CharField(label='ایمیل ',
                         widget=forms.EmailInput(attrs={'class':'form-control','placeholder':' ایمیل'}),
                         required=False
                         )
    phone=forms.CharField(label='تلفن ثابت ',
                         widget=forms.TextInput(attrs={'class':'form-control','placeholder':' تلفن ثابت'}),
                         error_messages={'required':'این فیلد نمیتواند خالی باشد'}
                         )
    
    description=forms.CharField(label='توضیحات ',
                         widget=forms.Textarea(attrs={'class':'form-control','placeholder':' توضیحات','rows':'3'}),
                         required=False
                         )
    payment_type=forms.ChoiceField(label='روش پرداخت',
                                   choices=[(item.id,item) for item in payment.objects.all()],
                                   widget=forms.RadioSelect(),
                                   )
    