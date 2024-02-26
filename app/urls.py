from django.urls import path
from . import views

#Page URLs
urlpatterns = [
    path('homePage', views.home_page, name='homePage'),
    path('profile', views.profile, name='profile'),
] 