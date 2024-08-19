from django import forms
from django.contrib.auth.models import User
from .models import Doctor

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'phone_number', 
            'address', 
            'photo', 
            'qualification', 
            'specialist_field', 
            'documentation'
        ]
