from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import User

class ServiceProviderForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        email=forms.EmailField()
        model = User
        fields=['username','email','password1','password2']



    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_serviceprovider = True
        user.save()
        return user

class ServiceFinderForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        email=forms.EmailField()
        model = User
        fields=['username','email','password1','password2']



    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_servicefinder = True
        user.save()
        return user

