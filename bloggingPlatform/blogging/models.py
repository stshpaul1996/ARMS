from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel,on_delete = models.PROTECT)
    author = models.CharField(max_length = 150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


