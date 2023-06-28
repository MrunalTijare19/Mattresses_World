from django import forms
from app.models import Customer

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name','customer_mob_no','customer_address')
        
        widgets = {
            'customer_name':forms.TextInput(attrs={'class':'form-control'}),
            'customer_mob_no':forms.NumberInput(attrs={'class':'form-control'}),
            'customer_address':forms.Textarea(attrs={'class':'form-control'}),
        }