from django.db import models

# Create your models here.


class Task(models.Model):
    Title = models.CharField(max_length = 250)
    Description = models.TextField()
    Completed = models.BooleanField()
    Created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title