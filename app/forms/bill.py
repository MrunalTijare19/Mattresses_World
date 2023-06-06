# from django import forms
# from app.models import Product, Employee, Customer, Billing

# class CreateBillForm(forms.ModelForm):
#     class Meta:
#         model = Billing
#         fields = ('employee','customer','product','quantity','bill_amount')
        
#         widgets = {
#             'employee': forms.TextInput(attrs={'class':'form-control'}),
#             'customer': forms.TextInput(attrs={'class':'form-control'}),
#             'product': forms.TextInput(attrs={'class':'form-control'}),
#             'quantity': forms.NumberInput(attrs={'class':'form-control'}),
#             'bill_amount': forms.NumberInput(attrs={'class':'form-control'})
#         }



from django import forms
from django.forms import formset_factory
from app.models import Billing

class CreateBillForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizing form field widgets or attributes
        self.fields['employee'].widget.attrs['class'] = 'form-control'
        self.fields['customer'].widget.attrs['class'] = 'form-control'
        self.fields['product'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
    

