
from django.urls import path
from hospital.views import Home, About

urlpatterns = [
    path('',Home,name='home'),
    path('about',About,name='about'),
   
]
