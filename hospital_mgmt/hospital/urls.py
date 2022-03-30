
from django.urls import path
from .views import Home, About, Service, Contact

urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('service/',Service,name='service'),
    path('contact/',Contact,name='contact'),
   
]
