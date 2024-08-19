from django.shortcuts import render, redirect
from .forms import DoctorForm, UserForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def doctor_register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        doctor_form = DoctorForm(request.POST, request.FILES)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            doctor = doctor_form.save(commit=False)
            doctor.user = user
            doctor.save()

            auth_login(request, user)
            return redirect('doctor_register_success')
    else:
        user_form = UserForm()
        doctor_form = DoctorForm()
    
    return render(request, 'auth/doctor_register.html', {
        'user_form': user_form,
        'doctor_form': doctor_form
    })

def doctor_register_success(request):
    return render(request, 'auth/doctor_register_success.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'auth/doctor_login.html')

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('auth/login')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')