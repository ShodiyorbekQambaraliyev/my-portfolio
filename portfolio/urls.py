from  django.urls import path
from  .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about-me/', about_me, name='about-me'),
    path('my_projects/', my_projects, name='my_projects'),
]