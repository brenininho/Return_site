from .models import Employees, Tasks
from django.shortcuts import render, redirect
from .forms import EmployeeForm
import ipdb


def list_employees(request):
    employees = Employees.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'manage_employees/crud_employees.html', context)


def create_employees(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'manage_employees/create_update_employee.html', {'form': form})


def update_employee(request, id):
    employee = Employees.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'manage_employees/create_update_employee.html', {'form': form, 'employee': employee})


def delete_employee(request, id):
    employee = Employees.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('/')

    return render(request, 'manage_employees/employee_delete.html', {'employee': employee})


def profile_employee(request, id):
    employee_id = Employees.objects.get(id=id)

    data = {
        'employee': employee_id
    }
    return render(request, 'manage_employees/profile_employee.html', data)
