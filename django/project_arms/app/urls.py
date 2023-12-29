from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addaspirant/',views.add_aspirant_view),
    path('aspirant/',views.aspirant_view, name='aspirant'),
    path('delete/<int:id>/',views.delete_aspirant_view,name='delete'),
    path('update/<int:id>/',views.update_aspirant_view,name='update'),
]