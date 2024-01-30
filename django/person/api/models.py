from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField(max_length=250, default="")
    age = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,null=True,related_name='created')
    updated_by = models.ForeignKey(User,on_delete=models.PROTECT,null=True,related_name='updated')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(null=True,blank=True)

    # def save(self, *args, **kwargs):
    #     # Update created_date only if the record is being created
    #     # import pdb;pdb.set_trace()
    #     if not self.pk:
    #         # Set created_by to the user creating the record
    #         user_creating = kwargs.get('created_by', None)
    #         self.created_by = user_creating
    #         self.updated_by = None  # Set updated_by to null when creating a record
    #         self.updated_date = None  # Set updated_date to null when creating a record

    #     # If the record is being updated
    #     else:
    #         # Set updated_by to the user updating the record
    #         user_updating = kwargs.get('updated_by', None)
    #         self.updated_by = user_updating
    #         self.updated_date = None

    #         updated_date_str = kwargs.get('updated_date', None)
    #         if updated_date_str:
    #             self.updated_date = updated_date_str
    #     super().save(*args, **kwargs)