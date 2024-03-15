from django.contrib import admin
from .models import Profile
from .models import Item, Avatar, OwnedItem

# Allows admins to read and modify user profiles
admin.site.register(Profile)
# Allow admins to upload and edit avatar images
admin.site.register([Item, Avatar, OwnedItem])

