from django.db import models

def doctor_image_upload_path(instance, filename):
    return f'doctor_images/{filename}'

def doctor_doc_upload_path(instance, filename):
    return f'doctor_docs/{filename}'

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to=doctor_image_upload_path)
    qualification = models.CharField(max_length=255)
    specialist_field = models.CharField(max_length=255)
    documentation = models.FileField(upload_to=doctor_doc_upload_path)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
