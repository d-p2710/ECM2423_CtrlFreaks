from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .models import Marker
from django.http import JsonResponse

urlpatterns = [
    path('word_searchGame/', views.word_search_game, name='word_search_game'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)