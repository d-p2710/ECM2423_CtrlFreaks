from django.shortcuts import render
from PIL import Image
from io import BytesIO
import base64
from users.models import Profile
from app.models import Marker
import qrcode

def home_page(request):
    return render(request, 'app/homePage.html')

def profile(request):
    marker = request.user.id
    data = Profile.objects.filter(user=marker).values
    context = {
        'data': data
    }
    return render(request, 'app/profilePage.html', context)
# Create your views here.

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
    markers = Marker.objects.all()
    context = {
        'markers': markers
    }
    return render(request, 'app/gameMap.html', context)

def logout(request):
    if request == 'POST':
        logout(request)