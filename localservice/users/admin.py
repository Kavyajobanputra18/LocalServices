from django.contrib import admin
from .models import User,ServiceFinder,ServiceProvider,Services

# Register your models here.
admin.site.register(User)
admin.site.register(ServiceProvider)
admin.site.register(ServiceFinder)
admin.site.register(Services)
