from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom Patient Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, password=None, password2=None):
      """
      Creates and saves a Patient with the given email, name and password.
      """
      if not email:
          raise ValueError('Patient must have an email address')
      
      if password != password2:
          raise ValueError("Password doesn't match!")

      patient = self.model(
          email=self.normalize_email(email),
          name=name,
      )

      patient.set_password(password)
      patient.save(using=self._db)
      return patient

#  Custom Patient Model
class Patient(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email