
from django.urls import path
from .views import Add_Appointment, Add_Patient, Delete_Appointment, Delete_Patient, Index, About,Logout, Service, Contact, Login,Dashboard, View_Appointment, View_Doctor,Delete_Doctor,Add_Doctor, View_Patient


urlpatterns = [
    path('',Index,name='index'),
    path('about/',About,name='about'),
    path('service/',Service,name='service'),
    path('contact/',Contact,name='contact'),

    # url path for admin
    path('admin_login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('dashboard/',Dashboard,name='dashboard'),

    # url path for doctors
    path('add_doctor/',Add_Doctor,name='add_doctor'),
    path('view_doctor/',View_Doctor,name='view_doctor'),
    path('delete_doctor(<int:id>)/',Delete_Doctor,name='delete_doctor'),

    # url paths for patient
    path('add_patient/',Add_Patient,name='add_patient'),
    path('view_patient/',View_Patient,name='view_patient'),
    path('delete_patient(<int:id>)/',Delete_Patient,name='delete_patient'),
    
#   url path for appointment
    path('add_appointment/',Add_Appointment,name='add_appointment'),
    path('view_appointment/',View_Appointment,name='view_appointment'),
    path('delete_appointment(<int:id>)/',Delete_Appointment,name='delete_appointment'),
]


