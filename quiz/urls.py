from django.urls import include, path
from . import views

app_name = "quiz"
urlpatterns = [
    path("<int:quiz_id>/start", views.start, name="start"),
    path("<int:quiz_id>/questions", views.question, name="question"),
    path("postAnswers", views.post_answers, name="postAnswers"),
    path("<int:quiz_id>/results", views.results, name="results"),
]