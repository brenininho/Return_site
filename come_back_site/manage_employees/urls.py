from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import list_employees, create_employees, update_employee, delete_employee, create_task, list_tasks, update_task, profile_employee


app_name = 'manage_employees'

urlpatterns = [
    path('', list_employees, name='list_employees'),
    path('tasks', list_tasks, name='list_tasks'),
    path('profile/<int:id>/', profile_employee, name='profile_employee'),
    path('new', create_employees, name='create_employees'),
    path('new_tasks', create_task, name='create_task'),
    path('update/<int:id>/', update_employee, name='update_employee'),
    path('update_task/<int:id>/', update_task, name='update_task'),
    path('delete/<int:id>/', delete_employee, name='delete_employee'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
