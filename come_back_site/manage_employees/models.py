from django.db import models


class Employees(models.Model):
    employee_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    birthday_date = models.DateTimeField('data do aniversário')

    def __str__(self):
        return self.employee_name


class Tasks(models.Model):
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    tasks = models.CharField(max_length=200)

    def __str__(self):
        return self.tasks
