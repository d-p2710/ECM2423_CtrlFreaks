from django.db import models
from django.contrib.auth.models import User

# Creates a separate object that's linked to the user which stores additional information
class Profile(models.Model):
    # Model is one to one, so each one user links to one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    points_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
