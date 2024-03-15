from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .models import Marker
from django.http import JsonResponse

urlpatterns = [
    path('homePage/', views.home_page, name='home'),
    path('profile/', profile, name='profile'),
    path('qr-generator/', views.qr_generator, name='qr_generator'),
    path('qr-scanner/', qr_scanner, name='qr_scanner'),
    path('geolocationMap/', views.geolocation_map, name='geolocation_map'),
    path('gameMap/', views.game_map, name='game_map'),
    path('crosswordGame/', views.crossword_game, name='crossword_game'),
    path('pairsGame/', views.pairs_game, name='pairs'),
    path('getMarkers/', views.get_markers, name='getMarkers'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)