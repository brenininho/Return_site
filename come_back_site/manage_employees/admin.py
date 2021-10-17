from django.contrib import admin
from .models import Tasks, Employees


class TasksInline(admin.TabularInline):
    model = Tasks
    extra = 3


class EmployeesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['employee_name']}),
        ('Date information', {'fields': ['birthday_date'], 'classes': ['collapse']}),
    ]
    inlines = [TasksInline]
    list_display = ('employee_name', 'birthday_date')
    list_filter = ['birthday_date']


admin.site.register(Employees, EmployeesAdmin)
