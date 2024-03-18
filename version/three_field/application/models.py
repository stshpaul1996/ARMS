from django.db import models

# Create your models here.
class Employee(models.Model):
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()

    @property
    def summ(self):
        return self.english+self.maths+self.science

