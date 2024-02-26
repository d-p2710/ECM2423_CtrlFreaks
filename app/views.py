from django.shortcuts import render

def home_page(request):
    return render(request, 'app/homePage.html')

def profile(request):
    return render(request, 'app/profilePage.html')
# Create your views here.
