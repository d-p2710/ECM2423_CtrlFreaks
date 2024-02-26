from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homePage', views.home_page, name='homePage'),
    path('profile', views.profile, name='profile'),
    path('qr-generator/', views.qr_generator, name='qr_generator'),
    path('qr-scanner/', views.qr_scanner, name='qr_scanner'),
    path('geolocationMap/', views.geolocation_map, name='geolocation_map'),
    path('gameMap/', views.game_map, name='game_map'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)