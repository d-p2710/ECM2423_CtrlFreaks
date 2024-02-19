from django.urls import path
from . import views

urlpatterns = [
    path('qr-generator/', views.qr_generator, name='qr_generator'),
    path('qr-scanner/', views.qr_scanner, name='qr_scanner'),
]
