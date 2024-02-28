from django.db import models
from django.contrib.auth.models import User

from ECM2423_CtrlFreaks import settings


# Creates a separate object that's linked to the user which stores additional information
class Profile(models.Model):
    # Model is one to one, so each one user links to one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.FileField(default='Example_1.png', upload_to='profile_images')
    bio = models.TextField()
    points_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
