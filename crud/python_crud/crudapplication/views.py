from django.shortcuts import render,redirect
from crudapplication.models import Employee
from crudapplication.forms import EmployeeForm
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.db import models
# Create your views here.

def emp(request):
        print("this is request print",request)
        if request.method == 'POST':
            show  = request.POST.get("id",'default')
            print("zaid",show)
            #binding the data to the form
            form = EmployeeForm(request.POST)

            if form.is_valid():
                try:
                    
                    form.save()
                    return HttpResponseRedirect("/list/")
                except:
                    pass

        else:
            form = EmployeeForm()
        return render(request,"index.html",{'form':form})

def listShow(request):
    employees =  Employee.people.all()
    return render(request,'list.html',{'employees':employees})


def edit(request,id):
    employee = Employee.people.get(id=id)
    # binding the data to the form
    employee = {"id":employee.id,"eName":employee.eName , "eContact":employee.eContact , "eEmail":employee.eEmail}
    return render(request,"index.html",employee)    

def update(request,id):
            employee = Employee.people.get(id=id)
            # instance gives the id of that record if there is no id it will create a new instance and create a new record
            form = EmployeeForm(request.POST,instance=employee)
            if form.is_valid():
                try:
                    form.save()
                    return HttpResponseRedirect("/list/")
                except:
                    pass

            return render(request,"index.html",{'form':form})

def delete(request,id):
     employee = Employee.people.get(id=id)
     employee.delete()
     return redirect('/list')