from django.urls import path
from . import views

urlpatterns = [
    path('homePage', views.home_page, name='homePage'),
    path('profile', views.profile, name='profile'),
] 