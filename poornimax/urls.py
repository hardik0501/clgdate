from django.contrib import admin
from django.urls import path, include
from . import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('poornima_site.urls')),
    path('accounts/', include('accounts.urls')), 
    path('feed/', include('feed.urls')),
    path('chat/', include('chat.urls', namespace='chat')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)