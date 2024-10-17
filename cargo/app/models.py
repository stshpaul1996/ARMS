from django.db import models

# Create your models here.

class HazardousMaterial(models.Model):
    un_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    placard_image_url = models.URLField()

    def __str__(self):
        return f"{self.name} (UN {self.un_number})"

class TransportRecord(models.Model):
    material = models.ForeignKey(HazardousMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()
    mixed_quantity = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transport Record for {self.material.name}"

class Invoice(models.Model):
    transport_record = models.ForeignKey(TransportRecord, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id} for Transport Record {self.transport_record.id}"
