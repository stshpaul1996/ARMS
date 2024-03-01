from django.db import models

class Abstract(models.Model):
    created_by = models.IntegerField(null=True)
    update_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Vehicle(Abstract):
    type_of_vehicle = models.CharField(max_length=20)
    no_of_seats = models.IntegerField()
    vehicle_no = models.CharField(max_length=50, unique=True)

class Trip(Abstract):
    vehicles = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_people = models.IntegerField()


