from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient, Doctor

class PatientRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth', 'gender', 'address']

    def save(self, commit=True):
        user = super().save(commit=commit)
        patient = Patient(user=user, date_of_birth=self.cleaned_data['date_of_birth'],
                          gender=self.cleaned_data['gender'], address=self.cleaned_data['address'])
        if commit:
            patient.save()
        return user

class DoctorRegistrationForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    address = forms.CharField(widget=forms.Textarea)
    specialization = forms.CharField()
    years_of_experience = forms.IntegerField()
    qualification = forms.CharField()
    license_number = forms.CharField()
    documentation = forms.FileField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'photo', 'address', 'specialization',
                  'years_of_experience', 'qualification', 'license_number', 'documentation']

    def save(self, commit=True):
        user = super().save(commit=commit)
        doctor = Doctor(user=user, photo=self.cleaned_data['photo'], address=self.cleaned_data['address'],
                        specialization=self.cleaned_data['specialization'],
                        years_of_experience=self.cleaned_data['years_of_experience'],
                        qualification=self.cleaned_data['qualification'],
                        license_number=self.cleaned_data['license_number'],
                        documentation=self.cleaned_data['documentation'])
        if commit:
            doctor.save()
        return user
