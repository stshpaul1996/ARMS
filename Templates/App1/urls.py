
from django.urls import path
from App1.views import home_view
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    
    path("",home_view),

]+static("/static",document_root = settings.STATIC_ROOT)
