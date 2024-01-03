from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_email(value):
    if value.isdigit():
        raise ValidationError("expecting alphanueric values")
class Person(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, default="", validators=(validate_email,))
    age = models.IntegerField(default=0)

    def clean(self):
        import pdb;pdb.set_trace()
        print("hello")

