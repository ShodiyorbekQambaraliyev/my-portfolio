from django.shortcuts import render, get_object_or_404
from .models import Menu, Home, Skils, Project, Resume
from django.http import FileResponse
import os

def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu})

def home(request):
    home = Home.objects.all()
    skills = Skils.objects.all()
    projects = Project.objects.all()
    menu = Menu.objects.all()
    return render(request, 'home.html', {
        'home': home,
        'skills': skills,
        'projects': projects,
        'menu': menu
    })


def my_projects(request):
    projects = Project.objects.all()
    menu = Menu.objects.all()
    return render(request, 'my_projects.html', {
        'projects': projects,
        'menu': menu
    })

def about_me(request):
    menu = Menu.objects.all()
    return render(request, 'about_me.html', {
        'menu': menu
    })

def contact(request): 
    menu = Menu.objects.all()
    resumes = Resume.objects.all()
    return render(request, 'contact.html', {
        'menu': menu,
        'resumes': resumes
    })

def download_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    filepath = resume.file.path
    filename = os.path.basename(resume.file.name)
    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=filename)