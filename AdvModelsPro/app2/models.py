from django.db import models
from app1.models import UserProfile

# Create your models here.

class ProxyUserProfile(UserProfile):
    class Meta:
        proxy = True
    
    

'''
INPUT
name address   email        floor  resources
A   Bangalore   A1@gmail.com   1      CPU
C   Bangalore   C3@gmail.com   1      DESKTOP  
A   Bangalore   A2@gmail.com   1      CPU
A   Bangalore   A3@gmail.com   2      Keyboard
C   Bangalore   C1@gmail.com   1      CPU
B   Bangalore   B1@gmail.com   2      DESKTOP
C   Bangalore   C2@gmail.com   2      Monitor  
B   Bangalore   B2@gmail.com   2      DESKTOP
B   Bangalore   B3@gmail.com   2      Monitor
OUTPUT
name total_visits most_visited_floor resources_used
A 3 1 CPU,DESKTOP
B 3 2 DESKTOP, MONITOR
C 3 1 DESKTOP, MONITOR, Keyboard

'''



class Visits(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    email = models.EmailField()
    floor = models.IntegerField()
    resources = models.CharField(max_length=100,)

    
   
    
