from django.urls import path
from app2.views import home,taj,sob,eiffeltower
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",home),
    path("Taj/",taj),
    path("Sob/",sob),
    path("Effiel/",eiffeltower),
]
#+static("/static",document_root=settings.STATIC_ROOT)
