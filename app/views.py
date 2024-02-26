from django.shortcuts import render

def home_page(request):
    return render(request, 'app/homePage.html')

# Create your views here.
