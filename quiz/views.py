from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
import json

from .models import Quiz, Question, Answer
from users.models import Profile

# auxiliary functions
def format_answers(answers_data):
    # group answers by question id
    formatted_answers = {}
    for entry in answers_data:
        question_id = entry.split("-")[0]
        if question_id not in formatted_answers.keys():
            formatted_answers[question_id] = [] 
        formatted_answers[question_id].append(answers_data[entry])
    return formatted_answers

def calculate_score(results_dict):
    score = 0
    for question_id in results_dict:
        #TODO decide on scoring system for different types of questions
        answer_ids = results_dict[question_id]
        question = get_object_or_404(Question, pk=int(question_id))
        if question.question_type == "SIN":
            # award a flat 2 marks if user gave the question's only correct answer
            answer = get_object_or_404(Answer, pk=int(answer_ids[0]))
            if answer.is_correct == True:
                score += 2
        elif question.question_type == "OOM":
            # award marks based on proportion of correct answers
            correct_answers = 0
            for answer_id in answer_ids:
                answer = get_object_or_404(Answer, pk=int(answer_id))
                if answer.is_correct:
                    correct_answers += 1
            if correct_answers / question.answer_set.filter(is_correct=True).count() == 1:
                score += 3
            elif correct_answers / question.answer_set.filter(is_correct=True).count() > 0.65:
                score += 1
    return score

@login_required
def start(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, "quiz/start.html", {"quiz": quiz})

@login_required
def question(request, quiz_id):
    # question_index starts at 1 for url readability
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, "quiz/question.html", {"quiz":quiz})

def post_answers(request):
    # dedicated backend view to process quiz rewards - prevents refreshing and resubmitting for rewards
    if request.method == "POST":
        # process POST request input
        post_dict = json.load(request)
        results_dict = format_answers(post_dict)
        score = calculate_score(results_dict)
        # save points and coins to database
        points = score * 100
        marker = request.user.id
        profile = Profile.objects.get(user=marker)
        profile.points_amount += points
        profile.coins_amount += score
        profile.save()
        return HttpResponse("success")

@login_required
def results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == "POST":
        # process POST request input
        request_as_dict = request.POST.dict()
        del request_as_dict["csrfmiddlewaretoken"]
        results_dict = format_answers(request_as_dict)
        answer_id_list = []
        for answer_list in results_dict.values():
            for answer_id in answer_list:
                answer_id_list.append(int(answer_id))        
        score = calculate_score(results_dict)
        context = {
                    "quiz": quiz,
                    "user_answers": answer_id_list,
                    "points": score * 100,
                    "coins": score,
                }
        return render(request, "quiz/results.html", context)

