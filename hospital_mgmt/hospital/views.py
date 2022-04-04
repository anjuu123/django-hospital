from distutils.log import error
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Appointment, Doctor, Patient

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
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d=0
    p=0
    a=0

    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    d1 = {'d':d, 'p':p, 'a':a}
    return render(request, 'dashboard.html',d1)


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
    if not request.user.is_staff:
        return redirect('login')
    error=""
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['mobile']
        ad = request.POST['address']
        try:

            Patient.objects.create(name=n, mobile=c, address=ad)
            error="no"
        except:
              error="yes"
    

    data = {'error':error}
    return render(request,'add_patient.html',data)




    # views all patients

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')

    pat = Patient.objects.all()
    data = {'pat': pat}
    return render(request, 'view_patient.html', data)

    



# delete patient by id
def Delete_Patient(request, id):
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id = id)
    patient.delete()
    return redirect('view_patient')


# add appointment
def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=="POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date=da, time=t)
            error="no"
        except:
            error="Yes"

    d = {'doctor': doctor1, 'patient': patient1, 'error': error }
    return render(request,'add_appointment.html',d)


  # views all appointment

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    apt = Appointment.objects.all()
    d = {'apt' : apt}
    return render(request, 'view_appointment.html', d)

# delete appointment by id
def Delete_Appointment(request, id):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id = id)
    appointment.delete()
    return redirect('view_patient')



