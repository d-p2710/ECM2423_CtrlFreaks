from django.db import models
from django.contrib.auth.models import User

#tw559
# Creates a separate object that's linked to the user which stores additional information
class Profile(models.Model):
    # Model is one to one, so each one user links to one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ForeignKey("Avatar", on_delete=models.CASCADE)
    bio = models.TextField()
    points_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

# zj274
# Create database models for storing and fetching avatar images
class AvatarPart(models.Model):
    PART_TYPES = {
        "colour": "Colour",
        "mouth": "Mouth",
        "eyes": "Eyes",
        "headwear": "Headwear",
        "accessory": "Accessory",
    }
    name = models.CharField(max_length=200)
    part_type = models.CharField(max_length=200, choices=PART_TYPES)
    img_file = models.ImageField("Image file", upload_to='profile_images')
    is_default_img = models.BooleanField("Default (image is default selection for this avatar part)", default=False)
    def __str__(self):
        return self.name

class Avatar(models.Model):
    # links a profile to the user's selected avatar parts
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    colour = models.ForeignKey(AvatarPart, null=True,
                                on_delete=models.CASCADE,
                                limit_choices_to={"part_type": "colour"},
                                related_name="+",)
    mouth = models.ForeignKey(AvatarPart, null=True,
                                on_delete=models.CASCADE,
                                limit_choices_to={"part_type": "mouth"},
                                related_name="+",)
    eyes = models.ForeignKey(AvatarPart, null=True,
                                on_delete=models.CASCADE,
                                limit_choices_to={"part_type": "eyes"},
                                related_name="+",)
    headwear = models.ForeignKey(AvatarPart, null=True,
                                on_delete=models.CASCADE,
                                limit_choices_to={"part_type": "headwear"},
                                related_name="+",)
    accessory = models.ForeignKey(AvatarPart, null=True,
                                on_delete=models.CASCADE,
                                limit_choices_to={"part_type": "accessory"},
                                related_name="+",)
    def __str__(self):
        return self.profile.user.username