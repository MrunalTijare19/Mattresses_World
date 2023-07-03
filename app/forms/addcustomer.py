from django import forms
from app.models import Customer

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name','customer_mob_no','customer_address')
        
        widgets = {
            'customer_name':forms.TextInput(attrs={'class':'form-control'}),
            'customer_mob_no':forms.NumberInput(attrs={'class':'form-control', 'type': 'number'}),
            'customer_address':forms.Textarea(attrs={'class':'form-control'}),
        }
        
    def clean_quantity(self):
        customer_mob_no = self.cleaned_data['customer_mob_no']
        if customer_mob_no < 0:
            raise forms.ValidationError("Mobile number cannot be negative.")
        return customer_mob_no