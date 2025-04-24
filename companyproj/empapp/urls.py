from django.urls import path
from . import views
urlpatterns = [
    path('emp_list/', views.emp_list, name='emp_list'), #1
    path('create/', views.create_employee, name='create_employee'), #1
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'), 
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'), #1
]
