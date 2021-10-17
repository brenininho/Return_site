from django import forms
from .models import Employees


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['employee_name', 'email', 'birthday_date']
