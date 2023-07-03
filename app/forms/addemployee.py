from django import forms
from app.models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_name','employee_mobile_no','employee_address','employee_salary')
        
        widgets = {
            'employee_name':forms.TextInput(attrs={'class':'form-control'}),
            'employee_mobile_no':forms.NumberInput(attrs={'class':'form-control', 'type': 'number'}),
            'employee_address':forms.TextInput(attrs={'class':'form-control'}),
            'employee_salary':forms.NumberInput(attrs={'class':'form-control', 'type': 'number'}),
        }


    def clean_quantity(self):
        employee_mobile_no = self.cleaned_data['employee_mobile_no']
        if employee_mobile_no < 0:
            raise forms.ValidationError("Mobile number cannot be negative.")
        return employee_mobile_no
    
    def clean_quantity(self):
        employee_salary = self.cleaned_data['employee_salary']
        if employee_salary < 0:
            raise forms.ValidationError("Salary cannot be negative.")
        return employee_salary
    


