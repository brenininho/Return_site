from .models import Employees, Tasks
from django.shortcuts import render, redirect
from .forms import EmployeeForm


def list_employees(request):
    employees = Employees.objects.all()
    return render(request, 'crud_employees.html', {'employees': employees})


def create_employees(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_employees')
    return render(request, 'create+update_employee.html', {'form': form})


def update_employee(request, id):
    employee = Employees.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('list_employees')

    return render(request, 'create+update_employee.html', {'form': form, 'employee': employee})


def delete_employee(request, id):
    employee = Employees.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('list_employees')

    return render(request, 'employee_delete.html', {'employee': employee})
