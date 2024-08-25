from django.urls import path
from . import views

urlpatterns = [
    path('register/patient/', views.register_patient, name='register_patient'),
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('login/patient/', views.login_patient, name='login_patient'),
    path('login/doctor/', views.login_doctor, name='login_doctor'),
]
