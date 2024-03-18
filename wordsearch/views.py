from django.shortcuts import render
from .models import CrosswordQuestion
from django.http import HttpResponse
from django.http import JsonResponse
from .trial import Crossword, Word
import random

# Create your views here.
# crossword game view
def word_search_game(request):
    #  Gets level info from cookie else defaults to 1
    level = int(request.COOKIES.get('level', 1))
    easy, medium, hard  = question_amount(level)
    easy_questions, medium_questions, hard_questions = get_words_search_questions(easy, medium, hard)

    easy_answers = [question.answer for question in easy_questions ]
    medium_answers = [question.answer for question in medium_questions ]
    hard_answers = [question.answer for question in hard_questions ]

    all_questions = easy_questions + medium_questions + hard_questions
    all_answers = easy_answers + medium_answers + hard_answers

    # Shuffle questions and answers
    combined = list(zip(all_questions, all_answers))
    random.shuffle(combined)
    all_questions, all_answers = zip(*combined)

     # Generate word search grid
     available_words = [(question.answer, question.hint) for question in all_questions]
     word_search = Crossword(15, 15, available_words=available_words)
     word_search.compute_crossword()

     # Get word search grid and legend
     grid = word_search.word_find()
     legend = word_search.legend()

     return render(request, 'wordsearch/wordsearch.html', {
         'grid': grid,
         'legend': legend
     })
# Function that dictates how many easy, hard, and medium questions are generated based on the user's level of difficulty
def question_amount(level):
    easy = medium = hard = 0

    # The pattern for easy & medium questions
    easy_medium_pattern = [(6, 0), (5, 1), (4, 2), (3, 3), (2,4), (1, 5), (0, 6)]

    # Calculate the index based on level
    pattern_index = (level - 1) % len(easy_medium_pattern)
    easy, medium = easy_medium_pattern[pattern_index]
    hard = (level - 1) // 7
    return  easy, medium, hard


def get_word_search_questions(easy, medium, hard):
    # Get the questions from the DB
    easy_questions = WordSearchQuestion.objects.filter(level=easy).order_by('?')[:easy]
    medium_questions  = WordSearchQuestion.objects.filter(level=medium).order_by('?')[:medium]
    hard_questions  = WordSearchQuestion.objects.filter(level=hard).order_by('?')[:hard]
    return easy_questions, medium_questions, hard_questions