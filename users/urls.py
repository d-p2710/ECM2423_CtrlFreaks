from django.urls import path
from .views import home, RegisterView, profile, terms

# Separate url directory for user based pages (specifically registration and profile)

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('terms/', terms, name='users-terms'),
]
