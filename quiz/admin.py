from django.contrib import admin
from .models import Quiz, Question, Answer

# Register your models here.
admin.site.register([Quiz, Question, Answer])