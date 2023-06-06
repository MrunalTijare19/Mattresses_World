from django import forms
from app.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['products', 'quantities']
