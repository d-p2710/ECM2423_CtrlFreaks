from django.urls import include, path
from . import views

app_name = "quiz"
urlpatterns = [
    path("<int:quiz_id>/start", views.start, name="start"),
    path("<int:quiz_id>/q<int:question_index>", views.question, name="question"),
    path("<int:quiz_id>/results", views.results, name="results"),
]