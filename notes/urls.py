from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from notes.views import *

urlpatterns = [
    path('', home, name='home.html')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)