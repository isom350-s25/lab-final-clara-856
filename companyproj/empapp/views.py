from django.shortcuts import render,redirect,get_object_or_404
from django.utils.text import slugify
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def emp_list(request): #1
    employees = Employee.objects.all() #2
    context = {
        'employees': employees #3
    }
    return render(request, "emp_list.html", context) #4
def create_employee(request):
    form = EmployeeForm(request.POST or None)

    data = {}
    data["form"] = form
    if form.is_valid():
        form.save() 
        return redirect("emp_list") 
    return render(request, "create_employee.html", data)

def edit_employee(request, id):
    p = get_object_or_404(Employee, id=id)  
    f = EmployeeForm(request.POST or None, instance=p)  

    data = {
        "form": f,
        "post": p
    }

    if f.is_valid():  
        f.save()  
        return redirect("emp_list")  
    
    return render(request, 'edit_employee.html', data)  #
def delete_employee(request,id):
    p = get_object_or_404(Employee,id = id)
    p.delete()
    return redirect("emp_list")