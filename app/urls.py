from django.urls import path
from . import views

urlpatterns = [
    path('home_page', views.home_page, name='homePage'),
] 