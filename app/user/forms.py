from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient, Doctor

class PatientRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField()
    gender = forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'gender', 'address', 'password1', 'password2')

class DoctorRegistrationForm(UserCreationForm):
    photo = forms.ImageField()
    address = forms.CharField(max_length=255)
    specialization = forms.CharField(max_length=255)
    years_of_experience = forms.IntegerField()
    qualification = forms.CharField(max_length=255)
    license_number = forms.CharField(max_length=50)
    documentation = forms.FileField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'photo', 'address', 'specialization', 'years_of_experience', 'qualification', 'license_number', 'documentation', 'password1', 'password2')
