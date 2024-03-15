from django.shortcuts import render
from PIL import Image
from io import BytesIO
import base64
from users.models import Profile, Avatar
from .models import CrosswordQuestion, Marker
from django.http import HttpResponse
from django.http import JsonResponse
from app.models import Marker

#page views
def home_page(request):
    return render(request, 'app/homePage.html')

def profile(request):
    marker = request.user.id
    profile = Profile.objects.filter(user=marker)[0]
    avatar = Avatar.objects.filter(profile=profile)[0]
    context = {
        'profile_data': profile,
        'avatar_data': avatar,
    }
    return render(request, 'app/profilePage.html', context)
    # return HttpResponse(avatar.colour.img_file.url)

#avatar shop views
# def avatar(request):
#     marker = request.user.id
#     if request.method == "POST":


#QR views
def qr_generator(request):
    context = {}
    if request.method == "POST":
        qr_text = request.POST.get("qr_text", "")
        qr_image = qrcode.make(qr_text, box_size=15)
        qr_image_pil = qr_image.get_image()
        stream = BytesIO()
        qr_image_pil.save(stream, format='PNG')
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
    return render(request, 'app/qrGenerator.html', context=context)

def qr_scanner(request):
    return render(request, 'app/qrScanner.html')


def geolocation_map(request):
    return render(request, 'app/geolocationMap.html')


def game_map(request):
    return render(request, 'app/gameMap.html')

#log in views
def logout(request):
    if request == 'POST':
        logout(request)

# crossword game view
def crossword_game(request):
    #  Gets level info from cookie else defaults to 1
    level = int(request.COOKIES.get('level', 1))
    easy, medium, hard  = question_amount(level)
    easy_questions, medium_questions, hard_questions = get_crossword_questions(easy, medium, hard)
    
    easy_answers = [question.answer for question in easy_questions ]
    medium_answers = [question.answer for question in medium_questions ]
    hard_answers = [question.answer for question in hard_questions ]
    return render(request, 'app/crosswordGame.html', {'easy_questions': easy_questions, 'medium_questions': medium_questions, 'hard_questions': hard_questions, 'easy_answers': easy_answers, 'medium_answers': medium_answers, 'hard_answers': hard_answers})

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


def get_crossword_questions(easy, medium, hard):
    # Get the questions from the DB
    easy_questions = CrosswordQuestion.objects.filter(level=easy).order_by('?')[:easy]
    medium_questions  = CrosswordQuestion.objects.filter(level=medium).order_by('?')[:medium]
    hard_questions  = CrosswordQuestion.objects.filter(level=hard).order_by('?')[:hard]
    return easy_questions, medium_questions, hard_questions

def pairs_game(request):
    # Example: Read session/cookie value
    username = request.session.get('username')
    card_level = int(request.COOKIES.get('card_level', 1))
    return render(request, 'app/pairs.html', {'username': username, 'card_level': card_level})

def get_markers(request):
    markers = Marker.objects.all()
    markers_data = [
        {
            "id": marker.id,
            "latitude": marker.latitude,
            "longitude": marker.longitude,
        }
        for marker in markers
    ]
    return JsonResponse(markers_data, safe=False)