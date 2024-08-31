from django.shortcuts import get_object_or_404, render, redirect
from dashboard.forms import DoctorEditForm, PatientEditForm, UserEditForm
from user.models import Doctor, Patient
from dashboard.utilis import handle_login
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        handle_login(request, email, password)

    return render(request, 'dashboard/das_home.html')

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('dashboard:home')

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('registerEmail')
        password = request.POST.get('registerPassword')
        
        user = authenticate(request, username=username, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have Successfully Registered and Logged In!")
        else:
            messages.error(request, "Invalid email or password to register. Please try again!")
    
    return render(request, 'dashboard/login.html', {'title': 'Register'})

User = get_user_model()

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'dashboard/user_list.html', {'users': users})

@login_required
def doctor_list(request):
    doctors = Doctor.objects.select_related('user').all()
    return render(request, 'dashboard/doctor_list.html', {'doctors': doctors})

@login_required
def patient_list(request):
    patients = Patient.objects.select_related('user').all()
    return render(request, 'dashboard/patient_list.html', {'patients': patients})


@login_required
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    user_form = UserEditForm(instance=doctor.user)
    doctor_form = DoctorEditForm(instance=doctor)
    
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=doctor.user)
        doctor_form = DoctorEditForm(request.POST, request.FILES, instance=doctor)
        
        if user_form.is_valid() and doctor_form.is_valid():
            user_form.save()
            doctor_form.save()
            messages.success(request, 'Doctor details updated successfully.')
            return redirect('dashboard:doctor_list')
        else:
            messages.error(request, 'Please correct the error below.')

    return render(request, 'dashboard/edit_doctor.html', {
        'user_form': user_form,
        'doctor_form': doctor_form,
    })
    
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        form = PatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient details updated successfully.')
            return redirect('dashboard:patient_list') 
    else:
        form = PatientEditForm(instance=patient)
    
    return render(request, 'dashboard/edit_patient.html', {'form': form, 'patient': patient})