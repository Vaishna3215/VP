from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Users


def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def sign(request):
    return render(request,'signup.html')

def newlogin(request):
    return render(request,'newlogin.html')

def newlogin(request):
    if request.method =="POST":
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        userdata=Users(name=name,username=username,password=password,email=email,phone=phone)
        userdata.save()
        return render(request,'newlogin.html')
    else:
            return render(request,'newlogin.html')


def indexe(request):
    return render(request,'indexe.html')

def register(request):
    return render(request,'register.html')

def loginadmin(request):
    return render(request,'loginadmin.html')

def adminhome(request):
    return render(request,'adminhome.html')

def employee(request):
    return render(request,'employee.html')


def exampy(request):
    if request.method =="POST":
     name=request.POST['value1']
     place=request.POST['value2']
     email=request.POST['value3']
     address=request.POST['value4']
     username=request.POST['value5']
     password=request.POST['value6']
    userdata=exampy(name=name, place=place,email=email,address=address,username=username,password=password)
    userdata.save()
    return render(request,'register.html')



        



