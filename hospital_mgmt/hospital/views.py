from distutils.log import error
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Doctor

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Service(request):
    return render(request, 'service.html')

def Dashboard(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'dashboard.html')


# login view
def Login(request):
    error = ""
    if request.method=="POST":
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        user = authenticate(username= uname, password = pwd )
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
    
            else:
                error = "yes"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


    # logout views

def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
        
    logout(request)
    return redirect('index')



# views all doctors

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc' : doc}
    return render(request, 'view_doctor.html', d)

# delete doctor by id
def Delete_Doctor(request, id):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id = id)
    doctor.delete()
    return redirect('view_doctor')

# add doctor
def Add_Doctor(request):
    error=""
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['mobile']
        sp = request.POST['speciality']
        try:
            Doctor.objects.create(name=n, mobile=c, speciality = sp)
            error="no"
        except:
            error="Yes"

    d = {'error':error}
    return render(request,'add_doctor.html',d)