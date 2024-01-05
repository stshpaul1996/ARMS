
from django.urls import path
from .views import postView,commentView

urlpatterns = [
    
    path("post/",postView.as_view()),
    path("post/<int:id>",postView.as_view()),
    path("comment/<int:id>",commentView.as_view()),
    path("comment/",commentView.as_view()),
]