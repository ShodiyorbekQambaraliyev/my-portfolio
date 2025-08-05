from django.shortcuts import render
from .models import Menu, Home

def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu})

def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {'home': home})

def my_projects(request):
    return render(request, 'my_projects.html')

def about_me(request):
    return render(request, 'about_me.html')

def contact(request): 
    return render(request, 'contact.html')