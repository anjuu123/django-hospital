from distutils.log import error
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Service(request):
    return render(request, 'service.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


# login view
def Login(request):
    error = ""
    if request.method=="POST":
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        user = authenticate(username= uname, password = pwd )
        try:
            if user.is_staff:
                Login(request,user)
                error = "No"

            else:
                error = "yes"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


    # logout views

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('login')



