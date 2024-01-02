
from django.urls import path
from .views import TodosView

urlpatterns = [
    
    path('todos/',TodosView.as_view()),
    path('todos/<int:id>',TodosView.as_view())
]