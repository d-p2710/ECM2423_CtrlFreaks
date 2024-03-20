from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    topics = models.CharField(max_length=200, blank=True, default="")
    def __str__(self):
        return self.title

class Question(models.Model):
    SINGLE_ANS = "SIN"
    ONE_OR_MORE_ANS = "OOM"
    QUESTION_TYPES = {
        SINGLE_ANS: "Single correct answer",
        ONE_OR_MORE_ANS: "One or more correct answers",
    }
    quiz = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES)
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField()
    def __str__(self):
        return self.text
