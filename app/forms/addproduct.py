from django import forms
from app.models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','description','price','quantity')
        
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control','Placeholder':'Product Name'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
        }
        
        
        
        
        