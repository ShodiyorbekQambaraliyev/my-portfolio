from django.shortcuts import render
from .models import Menu

def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu})

def home(request):
    return render(request, 'home.html')

def my_projects(request):
    return render(request, 'my_projects.html')

def about_me(request):
    return render(request, 'about_me.html')

def contact(request): 
    return render(request, 'contact.html')