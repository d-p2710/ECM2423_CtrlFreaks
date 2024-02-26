from django.contrib import admin
from .models import Profile

# Allows admins to read and modify user profiles
admin.site.register(Profile)
