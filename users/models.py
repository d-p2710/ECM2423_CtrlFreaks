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
    coins_amount = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

# zj274
# Create database models for storing and fetching avatar images
class Item(models.Model):
    CATEGORIES = {
        "colour": "Colour",
        "mouth": "Mouth",
        "eyes": "Eyes",
        "headwear": "Headwear",
        "accessory": "Accessory",
    }
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORIES)
    price = models.IntegerField()
    img_file = models.ImageField("Image file", upload_to='profile_images')
    is_default_img = models.BooleanField("Default (image is default selection for this item)", default=False)
    def __str__(self):
        return self.name

class Avatar(models.Model):
    # links a profile to the user's selected avatar parts
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    colour = models.ForeignKey(Item, on_delete=models.CASCADE,
                                limit_choices_to={"category": "colour"},
                                related_name="+",)
    mouth = models.ForeignKey(Item, on_delete=models.CASCADE,
                                limit_choices_to={"category": "mouth"},
                                related_name="+",)
    eyes = models.ForeignKey(Item, on_delete=models.CASCADE,
                                limit_choices_to={"category": "eyes"},
                                related_name="+",)
    headwear = models.ForeignKey(Item, null=True,
                                on_delete=models.CASCADE,
                                limit_choices_to={"category": "headwear"},
                                related_name="+",)
    accessory = models.ForeignKey(Item, null=True,
                                on_delete=models.CASCADE,
                                limit_choices_to={"category": "accessory"},
                                related_name="+",)
    def __str__(self):
        return self.profile.user.username
    
class OwnedItem(models.Model):
    # resolves many-to-many relationship between User/Profile and AvatarPart
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)