from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Quiz, Question

# Create your views here.
def start(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, "quiz/start.html", {"quiz": quiz})

def end(request):
    return HttpResponse("End Screen")

def question(request, quiz_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "quiz/question.html", {"question": question})