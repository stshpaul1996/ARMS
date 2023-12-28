from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.

# def check_alpha(value):
#     if not value.isalpha():
#         raise ValidationError("Enter only characters")




class Resources(models.Model):
    first_name = models.CharField(max_length=250, )
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.BigIntegerField()
    graduation = models.CharField(max_length=500)
    stream = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    pg = models.CharField(max_length=500, null=True)
    pg_stream = models.CharField(max_length=100, null=True)
    pg_year = models.SmallIntegerField(null=True)
    trained_technology = models.CharField(max_length=250)
    institute_name = models.CharField(max_length=500)
    duration_course = models.CharField(max_length=100)
    reference_name = models.CharField(max_length=250, null=True)
    hear_interview = models.CharField(max_length=100, null=True)
    work_experience = models.CharField(max_length=100, null=True)
    years_experience = models.SmallIntegerField(null=True)
    company_name = models.CharField(max_length=500, null=True)
    current_ctc = models.FloatField(null=True)
    expected_ctc = models.FloatField(null=True)
    pf = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'id:{self.id} name:{self.first_name} {self.last_name}'


class Rounds(models.Model):
    online_marks = models.FloatField()
    is_online_passed = models.BooleanField(default=False)
    online_feedback = models.TextField()
    communication_marks = models.FloatField()
    is_communication_passed = models.BooleanField(default=False)
    communication_feedback = models.TextField()
    technical_marks = models.FloatField()
    is_technical_passed = models.BooleanField(default=False)
    technical_feedback = models.TextField()
    is_qualified = models.BooleanField(default=False)
    is_ceo_passed = models.BooleanField(default=False)
    resource_id = models.ForeignKey(Resources, on_delete=models.DO_NOTHING)

class OnBoarded(models.Model):
    onboard_status = models.BooleanField(default=False)
    rounds_id = models.ForeignKey(Rounds, on_delete=models.DO_NOTHING)


