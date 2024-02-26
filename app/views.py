from django.shortcuts import render

# Renders home page
def home_page(request):
    return render(request, 'app/homePage.html')

#Renders profile page
def profile(request):
    return render(request, 'app/profilePage.html')
# Create your views here.
