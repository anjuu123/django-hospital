from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Service(request):
    return render(request, 'service.html')