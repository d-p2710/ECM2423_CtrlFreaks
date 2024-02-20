from django.urls import path
from . import views

# app_name = "quiz"
urlpatterns = [
    path("", views.end, name="end"),
    path("<int:quiz_id>/", views.start, name="start"),
    path("<int:quiz_id>/q<int:question_index>", views.question, name="question"),
    # path("<int:question_id>/results/", views.results, name="results"),
]