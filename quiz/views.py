from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse

from .models import Quiz, Question, Answer

def start(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, "quiz/start.html", {"quiz": quiz})

def questions(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, "quiz/questions.html", {"quiz": quiz})

def results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    # process POST request input
    request_as_dict = request.POST.dict()
    del request_as_dict["csrfmiddlewaretoken"]
    results_data = {}
    answer_id_list = []
    # group answers by question id
    for entry in request_as_dict:
        question_id = entry.split("-")[0]
        if question_id not in results_data.keys():
            results_data[question_id] = [] 
        results_data[question_id].append(request_as_dict[entry])
        answer_id_list.append(int(request_as_dict[entry]))
    score = 0
    # calculate awarded points and save to user DB
    for question_id in results_data:
        #TODO decide on scoring system for different types of questions
        answer_ids = results_data[question_id]
        question = get_object_or_404(Question, pk=int(question_id))
        if question.question_type == "SIN":
            # award a flat 5 marks if user gave the question's only correct answer
            answer = get_object_or_404(Answer, pk=int(answer_ids[0]))
            if answer.is_correct == True:
                score += 5
        elif question.question_type == "OOM":
            # award marks based on proportion of correct answers
            correct_answers = 0
            for answer_id in answer_ids:
                answer = get_object_or_404(Answer, pk=int(answer_id))
                if answer.is_correct:
                    correct_answers += 1
            if correct_answers / question.answer_set.filter(is_correct=True).count() == 1:
                score += 10
            elif correct_answers / question.answer_set.filter(is_correct=True).count() > 0.4:
                score += 5
    return render(request, "quiz/results.html", {"quiz": quiz, "user_answers": answer_id_list})