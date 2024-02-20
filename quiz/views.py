from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Quiz, Question

def start(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, "quiz/start.html", {"quiz": quiz})

def end(request):
    return HttpResponse("End Screen")

def question(request, quiz_id, question_index):
    # Note that question_index starts at 1 for url readability
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(Question, pk=quiz.question_set.all()[question_index-1].id)
    # Query equates to "SELECT FROM Question WHERE Question.pk = id of the next question in the quiz"
    next_q_index = question_index + 1
    next_url = "/quiz/" + str(quiz_id) + "/q" + str(next_q_index)
    if next_q_index > quiz.question_set.count():
        # if on last question, set redirect to end screen
        next_url = "/quiz"
    return render(request, "quiz/question.html", {"question": question, "quiz":quiz, "next_url":next_url})