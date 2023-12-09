from django.db import models

# Create your models here.
class aspirants(models.Model):
    full_name = models.CharField(max_length=250)
    email_id = models.EmailField(max_length=250)
    phone_no = models.BigIntegerField()
    gradution = models.CharField(max_length=100)
    post_gradution = models.CharField(max_length=100,null=True)
    stream = models.CharField(max_length=100,null=True)
    passed_out_year = models.SmallIntegerField(null=True)
    trained_on_technology = models.CharField(max_length=100,null=True)
    institue_name = models.CharField(max_length=300,null=True)
    duration_of_course = models.SmallIntegerField(null=True)
    Reference_name = models.CharField(max_length=250,null=True)
    experience = models.SmallIntegerField(null=True)
    previous_company_name = models.CharField(max_length=250,null=True)
    current_ctc = models.BigIntegerField(null = True)
    expected_ctc = models.BigIntegerField(null = True)

class Rounds(models.Model):
    marks_onlinetest = models.SmallIntegerField()
    isqualified_onlinetest = models.BooleanField(default=True)
    feedback_online = models.CharField(max_length=250)
    marks_communicationtest = models.SmallIntegerField()
    isqualified_communicationtest = models.BooleanField(default=True)
    feedback_communication = models.CharField(max_length=250)
    marks_technicaltest = models.SmallIntegerField()
    isqualified_technical = models.BooleanField(default=True)
    feedback_technical = models.CharField(max_length=250)
    is_selected = models.BooleanField(default=True)
    feedback = models.CharField(max_length=250)
    aspirantsid = models.ForeignKey(aspirants,on_delete=models.PROTECT)

class onboared(models.Model):
    is_onboared = models.BooleanField(default=True)
    aspirantsid = models.ForeignKey(aspirants,on_delete=models.PROTECT)
