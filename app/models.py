from django.db import models


# Create your models here.

class Marker(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    

    def __str__(self):
        return self.name

class QRCode(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    qr_image_base64=models.BinaryField()

    def __str__(self) -> str:
        return self.name

class CrosswordQuestion(models.Model):
    hint = models.CharField(max_length=500)
    answer = models.CharField(max_length=200)
    level = models.CharField(max_length=10, choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")])
