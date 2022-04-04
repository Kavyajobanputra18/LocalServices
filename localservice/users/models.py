from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_serviceprovider = models.BooleanField(default=True)
    is_servicefinder = models.BooleanField(default=True)

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class ServiceFinder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

