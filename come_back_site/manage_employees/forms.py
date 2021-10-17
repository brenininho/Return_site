from django import forms
from .models import Employees, Tasks


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['employee_name', 'email', 'birthday_date']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['tasks', 'employees']
