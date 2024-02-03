from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class AbstractField(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    class Meta:
        abstract = True
    
class Joner(AbstractField):
    pass

class Movie(AbstractField):
    release_date = models.DateField()
    joner = models.ForeignKey(Joner,on_delete=models.PROTECT)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # created_date = models.DateTimeField(auto_now_add = True)
    # updated_date = models.DateTimeField(null = True, blank = True)
    # created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name = 'create')
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name = 'update')
    

