from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Doctor, Patient
from .forms import PatientRegistrationForm, DoctorRegistrationForm


def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'Patient'
            user.set_password(form.cleaned_data.get('password1'))
            user.save()

            patient = Patient.objects.create(
                user=user,
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                gender=form.cleaned_data.get('gender'),
                address=form.cleaned_data.get('address')
            )
            patient.save()

            messages.success(request, 'Patient registration successful.')
            return redirect('login_patient')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = PatientRegistrationForm()
    return render(request, 'user/register_patient.html', {'form': form})


def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'Doctor'
            user.set_password(form.cleaned_data.get('password1'))
            user.save()

            doctor = Doctor.objects.create(
                user=user,
                photo=form.cleaned_data.get('photo'),
                address=form.cleaned_data.get('address'),
                specialization=form.cleaned_data.get('specialization'),
                years_of_experience=form.cleaned_data.get('years_of_experience'),
                qualification=form.cleaned_data.get('qualification'),
                license_number=form.cleaned_data.get('license_number'),
                documentation=form.cleaned_data.get('documentation'),
                verification_status=False 
            )
            doctor.save()

            messages.success(request, 'Doctor registration successful.')
            return redirect('login_doctor')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'user/register_doctor.html', {'form': form})


def login_patient(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.user_type == 'Patient':
                login(request, user)
                return redirect('patient_dashboard')
            else:
                messages.error(request, 'Invalid credentials or user type.')
        else:
            print(form.errors)  
            messages.error(request, 'Invalid credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login_patient.html', {'form': form})


def login_doctor(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.user_type == 'Doctor':
                login(request, user)
                return redirect('doctor_dashboard')
            else:
                messages.error(request, 'Invalid credentials or user type.')
        else:
            print(form.errors)  
            messages.error(request, 'Invalid credentials.')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login_doctor.html', {'form': form})