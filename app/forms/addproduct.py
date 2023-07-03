from django import forms
from app.models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','description','price','quantity')
        
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control','Placeholder':'Product Name'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'type': 'number'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control', 'type': 'number'}),
        }
        
    def clean_quantity(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Product Price cannot be negative.")
        return price
        
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError("Product quantity cannot be negative.")
        return quantity
        
        
        