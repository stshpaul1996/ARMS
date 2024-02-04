from django.db import models

class Trip(models.Model):
    name = models.CharField(max_length=250)
    created_by = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_by = models.CharField(max_length=250, default="")
    updated_at = models.DateTimeField(null=True)
    


class Member(models.Model):
    name = models.CharField(max_length=250)
    trip = models.ForeignKey(Trip, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_by = models.CharField(max_length=250, default="")
    updated_at = models.DateTimeField(null=True)


class Expenses(models.Model):
    spent = models.IntegerField()
    spent_for = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_by = models.CharField(max_length=250, default="")
    updated_at = models.DateTimeField(null=True)


