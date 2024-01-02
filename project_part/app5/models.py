from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

def isalp(value):
    if not value.isalpha():
        raise ValidationError("please enter alphabets only")    
class Users(models.Model):
    first_name = models.CharField(max_length=250,validators=[isalp])
    last_name = models.CharField(max_length=250)
    email_id = models.EmailField(max_length=250)
    phone_no = models.BigIntegerField()
    graduation = models.CharField(max_length=100)
    graduation_stream = models.CharField(max_length=150)
    graduation_year = models.SmallIntegerField()
    post_graduation = models.CharField(max_length=100)
    post_graduation_stream = models.CharField(max_length=150)
    post_graduation_year = models.SmallIntegerField(default=0)
    trained_on_technology = models.CharField(max_length=250)
    institute_name = models.TextField(max_length=500)
    course_duration = models.CharField(max_length=100)
    reference_name = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    experience_years = models.SmallIntegerField(default=0)
    previous_company_name = models.TextField(max_length=500)
    current_ctc = models.BigIntegerField(default=0)
    expected_ctc = models.BigIntegerField(default=0)
    pf = models.BooleanField(default=0)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.id}'


class Rounds(models.Model):
    online_marks = models.FloatField()
    online_status = models.BooleanField(default=False)
    online_feedback = models.TextField()
    tech_marks = models.FloatField()
    tech_status  = models.BooleanField(default=False)
    tech_feedback = models.TextField()
    comm_marks = models.FloatField()
    comm_status  = models.BooleanField(default=False)
    comm_feedback = models.TextField()
    is_selected = models.BooleanField(default=False)
    user_id = models.ForeignKey(Users,on_delete=models.PROTECT)


class Joined(models.Model):
    is_joined = models.BooleanField()
    user_id = models.ForeignKey(Users,on_delete=models.PROTECT)
