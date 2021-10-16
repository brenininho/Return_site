from django.db import models


class Employees(models.Model):
    employee_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    cpf = models.IntegerField(default=11)
    birthday_date = models.DateTimeField('data do aniversário')

    def __str__(self):
        return self.employee_name


class Choice(models.Model):
    question = models.ForeignKey(Employees, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
