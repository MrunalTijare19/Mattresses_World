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
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.pk is None:  # Check if the instance is being created (not updated)
            last_customer = Customer.objects.order_by('-customer_id').first()
            if last_customer:
                instance.customer_id = last_customer.customer_id + 1
            else:
                instance.customer_id = 1
        if commit:
            instance.save()
        return instance