from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Custom User Model to include different user types
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    )
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set', 
        blank=True
    )

# Patient model extending User
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.user.get_full_name()
    
def doctor_image_upload_path(instance, filename):
    return f'doctor_images/{filename}'

def doctor_doc_upload_path(instance, filename):
    return f'doctor_docs/{filename}'

# Doctor model extending User
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=doctor_image_upload_path)
    address = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
    qualification = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50)
    verification_status = models.BooleanField(default=False)
    documentation = models.FileField(upload_to=doctor_doc_upload_path)

    def __str__(self):
        return self.user.get_full_name()