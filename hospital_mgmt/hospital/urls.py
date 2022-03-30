
from django.urls import path
from hospital.views import About

urlpatterns = [
    path('',About,name='about'),
   
]
