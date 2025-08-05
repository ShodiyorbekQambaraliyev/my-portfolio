from django.shortcuts import render


def menu(request):
    return render(request, 'menu.html')

def home(request):
    return render(request, 'home.html')

def my_projects(request):
    return render(request, 'my_projects.html')

def about_me(request):
    return render(request, 'about_me.html')

def contact(request):
    return render(request, 'contact.html')