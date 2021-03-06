from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "formcms/employee_list.html", context)

def employee_edit(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "formcms/employee_edit.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "formcms/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST, request.FILES)
        else:   
             employee = Employee.objects.get(pk=id)
             form = EmployeeForm(request.POST, request.FILES, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')