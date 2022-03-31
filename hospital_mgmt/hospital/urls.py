
from django.urls import path
from .views import Index, About, Logout, Service, Contact, Login,Dashboard
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',Index,name='index'),
    path('about/',About,name='about'),
    path('service/',Service,name='service'),
    path('contact/',Contact,name='contact'),
    path('admin_login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('dashboard/',Dashboard,name='dashboard'),
   
]


urlpatterns += staticfiles_urlpatterns()