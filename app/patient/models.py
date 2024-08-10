from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom Patient Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a Patient with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        patient = self.model(email=email, name=name)
        patient.set_password(password)
        patient.save(using=self._db)
        return patient

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        patient = self.create_user(
            email,
            name=name,
            password=password,
        )
        patient.is_admin = True
        patient.is_staff = True
        patient.save(using=self._db)
        return patient


class Patient(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
