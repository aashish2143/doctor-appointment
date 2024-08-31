from django import forms
from django.contrib.auth.models import User

from user.models import Doctor, Patient

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']

class DoctorEditForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['photo', 'specialization', 'years_of_experience', 'qualification', 'license_number', 'verification_status']
        
class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['user', 'date_of_birth', 'gender', 'address']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
