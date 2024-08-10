from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('patient:dashboard')
        else:
            messages.error(request, "Invalid email or password")
            return render(request, 'auth/patient_login.html')
    
    return render(request, 'auth/patient_login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'auth/patient_register.html')

        User = get_user_model()

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address already in use!")
            return render(request, 'auth/patient_register.html')

        # Check if the username (name) already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, 'auth/patient_register.html')

        try:
            User.objects.create_user(email=email, username=username, password=password)
            return redirect('patient:pa-login')
        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return render(request, 'auth/patient_register.html')

    return render(request, 'auth/patient_register.html')


def forgot_password_view(request):
    return render(request, 'auth/forgot_password.html')

def password_change_view(request):
    return render(request, 'auth/password_change.html')