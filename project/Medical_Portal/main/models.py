from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField()

class Medication(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    times = models.PositiveSmallIntegerField()
    notes = models.CharField(max_length=350)

    def __str__(self):
        return f"{self.name} for {self.patient}"


"""
############## Posts Model ################
- id
- Symptoms
- Medications
- Diagnoses
- Notes/description
"""

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms = models.CharField(max_length=300)
    medications = models.CharField(max_length=300)
    diagnosis = models.CharField(max_length=150)
    Notes = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']
        