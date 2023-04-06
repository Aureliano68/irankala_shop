from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .forms import commentForm
from apps.product.models import Product
from apps.coment_score_faw.models import Score
from django.http import HttpResponse
from .models import comment
from django.contrib import messages

# Create your views here.
# =============================================================================
class commentView(View):
    def get(self,request,*args,**kwargs):
        productid=request.GET.get('productid')
        commentid=request.GET.get('commentid')
        slug=kwargs['slug']
        initial_dict={
            'product_id':productid,
            'comment_id':commentid
        }
        form=commentForm(initial=initial_dict)
        context={
            'form':form,
            'slug':slug
        }
        return render(request,'csf/create_comment.html',context)
    
    def post(self,request,*args,**kwargs):
        slug=kwargs.get('slug')
        product=get_object_or_404(Product,slug=slug)
        form=commentForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            parent=None
            if (data['comment_id']):
                parentid=data['comment_id']
                parent=comment.objects.get(id=parentid)
                
            comment.objects.create(
                product=product,
                comment_user=request.user,
                comment_text=data['comment_text'],
                comment_parent=parent
            )
            messages.success(request,'اطلاعات با موفقیت ثبت شد','success')
            return redirect('product:Detail_Product',product.slug)
        messages.error(request,'خطا در ارسال نظر','danger')
        return redirect('product:Detail_Product',product.slug)
            
# =============================================================================
def add_score(request):
    productid=request.GET.get('productid')     
    score=request.GET.get('score') 
    
    product=Product.objects.get(id=productid)
    Score.objects.create(
        product=product,
        scoring_user=request.user,
        score=score
        
    )
    return HttpResponse('امتیاز شما با موفقیت ثبت شد')
    
            