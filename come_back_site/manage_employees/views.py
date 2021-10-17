from .models import Employees, Tasks
from django.shortcuts import render, redirect
from .forms import EmployeeForm, TaskForm


def list_employees(request):
    employees = Employees.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'manage_employees/crud_employees.html', context)


def list_tasks(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'manage_employees/tasks.html', context)


def create_employees(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'manage_employees/create_update_employee.html', {'form': form})


def create_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'manage_employees/create_update_task.html', {'form': form})


def update_employee(request, id):
    employee = Employees.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'manage_employees/create_update_employee.html', {'form': form, 'employee': employee})


def update_task(request, id):
    task = Tasks.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'manage_employees/create_update_task.html', {'form': form, 'task': task})


def delete_employee(request, id):
    employee = Employees.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('/')

    return render(request, 'manage_employees/employee_delete.html', {'employee': employee})
