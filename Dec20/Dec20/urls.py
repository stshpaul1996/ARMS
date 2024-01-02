from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1.views import media_view

urlpatterns = [
    path("", media_view),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)