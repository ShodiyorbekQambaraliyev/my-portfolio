from  django.urls import path
from  .views import *

urlpatterns = [
    path('', menu, name='menu'),
    path('home/', home, name='home'),
    path('my_projects/', my_projects, name='my_projects'),
    path('about_me/', about_me, name='about_me'),
]