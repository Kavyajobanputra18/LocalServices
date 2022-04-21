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

class Services(models.Model):
    service_name = models.CharField(max_length=30)
    service_description = models.TextField(null=True)

    class Meta():
        db_table = 'services'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

