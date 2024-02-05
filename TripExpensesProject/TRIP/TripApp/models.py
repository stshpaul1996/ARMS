from django.db import models


class Abstract(models.Model):
    created_by = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_by = models.CharField(max_length=250, default="")
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True

class Trip(Abstract):
    name = models.CharField(max_length=250)
    

class Member(Abstract):
    name = models.CharField(max_length=250)
    trip = models.ForeignKey(Trip, on_delete=models.PROTECT)
   

class Expenses(Abstract):
    spent = models.IntegerField()
    spent_for = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
  
