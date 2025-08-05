from  django.urls import path
from  .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', menu, name='menu'),
    path('home/', home, name='home'),
    path('my_projects/', my_projects, name='my_projects'),
    path('about_me/', about_me, name='about_me'),
    path('contact/', contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)