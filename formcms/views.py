from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeeForm

#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

def employee_list(request):
    return render(request, "formcms/employee_list.html")

def employee_form(request):
    form = EmployeeForm()
    return render(request, "formcms/employee_form.html", {'form':form} )

def employee_delete(request):
    return