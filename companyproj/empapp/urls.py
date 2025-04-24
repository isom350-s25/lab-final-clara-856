from django.urls import path
from . import views
urlpatterns = [
    path("", views.emp_list, name="emp_list"), 
    path('emp_list/', views.emp_list, name='emp_list'), 
    path('create/', views.create_employee, name='create_employee'), 
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'), 
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'), 
]
