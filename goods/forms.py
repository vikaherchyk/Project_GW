from django import forms

from goods.models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
    
    # name = forms.CharField()
    # slug = forms.CharField()
    
# class BookedForm(forms.ModelForm):
#     class Meta:
#         model = Booked
#         fields = ('username', 'email', 'phone_number', 'checkin', 'checkout',)
    
#     username = forms.ImageField()
#     email = forms.CharField()
#     phone_number = forms.CharField()
#     checkin = forms.CharField()
#     checkout = forms.CharField()
