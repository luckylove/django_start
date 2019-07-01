from django.contrib import admin

# Register your models here.
# register the profile models

from .models import Profile

admin.site.register(Profile)
