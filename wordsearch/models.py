from django.db import models

# Create your models here.
class WordSearchQuestion(models.Model):
    hint = models.CharField(max_length=500)
    answer = models.CharField(max_length=200)
    level = models.CharField(max_length=10, choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")])