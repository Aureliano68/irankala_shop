from django import forms

class commentForm(forms.Form):
    product_id=forms.CharField(widget=forms.HiddenInput(),required=False)
    comment_id=forms.CharField(widget=forms.HiddenInput(),required=False)

    comment_text=forms.CharField(
            label='',
            widget=forms.Textarea(attrs={'class':'form-control','placeholder':'  متن نظر'})
            

    )