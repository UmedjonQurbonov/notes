from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from notes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('notes/', include('notes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

