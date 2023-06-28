from django import forms
from app.models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_name','employee_mobile_no','employee_address','employee_salary')
        
        widgets = {
            'employee_name':forms.TextInput(attrs={'class':'form-control'}),
            'employee_mobile_no':forms.NumberInput(attrs={'class':'form-control'}),
            'employee_address':forms.TextInput(attrs={'class':'form-control'}),
            'employee_salary':forms.NumberInput(attrs={'class':'form-control'}),
        }





