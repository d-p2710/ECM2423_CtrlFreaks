from django.urls import path
from . import views

app_name = "quiz"
urlpatterns = [
    path("<int:quiz_id>/start", views.start, name="start"),
    path("<int:quiz_id>/", views.questions, name="questions"),
    path("<int:quiz_id>/results", views.results, name="results"),
]