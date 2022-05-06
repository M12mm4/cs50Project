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

