from distutils.log import error
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Doctor, Patient

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





# add patients
def Add_Patient(request):
    error=""
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['mobile']
        ad = request.POST['address']
        try:
            Patient.objects.create(name=n, mobile=c, address=ad)
            error="no"
        except:
            error="Yes"

    d = {'error':error}
    return render(request,'add_patient.html',d)

    # views all patients

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')

    pat = Patient.objects.all()
    d = {'pat' : pat}
    return render(request, 'view_patient.html', d)

# delete patient by id
def Delete_Patient(request, id):
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id = id)
    patient.delete()
    return redirect('view_patient')