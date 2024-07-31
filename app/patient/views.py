from django.shortcuts import render


def login_view(request):
    return render(request, 'auth/patient_login.html')

def register_view(request):
    return render(request, 'auth/patient_register.html')

def forgot_password_view(request):
    return render(request, 'auth/forgot_password.html')

def password_change_view(request):
    return render(request, 'auth/password_change.html')