
from django.urls import path
from .views import Index, About, Logout, Service, Contact, Login,Dashboard, View_Doctor,Delete_Doctor


urlpatterns = [
    path('',Index,name='index'),
    path('about/',About,name='about'),
    path('service/',Service,name='service'),
    path('contact/',Contact,name='contact'),
    path('admin_login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('dashboard/',Dashboard,name='dashboard'),
    path('view_doctor/',View_Doctor,name='view_doctor'),
    path('delete_doctor(<int:id>)/',Delete_Doctor,name='delete_doctor'),
   
]


