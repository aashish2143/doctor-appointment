from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    # Authentication
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    
    # List Display
    path('users/', views.user_list, name='user_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    
    # Edit 
    path('doctor/edit/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('patient/edit/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    
    # Delete
    path('patient/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('doctor/delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
]
