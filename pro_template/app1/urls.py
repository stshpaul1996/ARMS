from django.urls import path
from .views import home_view,kalam,singh,shivaji,ashoka
from django.conf.urls.static import static
urlpatterns = [
    
    path('',home_view),
    path('kalam/',kalam),
    path('sin/',singh),
    path('shivaji/',shivaji),
    path('ashoka/',ashoka)
    
]
