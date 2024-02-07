from django.db import models

# Create your models here.
class AbstractModel(models.Model):
    created_by = models.CharField(max_length =100,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100,null = True)


    class Meta:
        abstract = True

class Vehicle(AbstractModel):
    vehicle_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    capacity = models.IntegerField()

    

class Trip(AbstractModel):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    num_of_people = models.IntegerField()

    
