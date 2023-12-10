from django.db import models

# Create your models here.
class Aspirant(models.Model):
    id=models.BigAutoField(primary_key=True)
    Application_no=models.IntegerField()
    Full_name=models.CharField(max_length=100)
    Email_id=models.EmailField(max_length=100)
    Phone_no=models.BigIntegerField()
    Graduation=models.CharField(max_length=100)
    Graduation_Stream=models.CharField(max_length=100)
    Passed_Out_Year=models.IntegerField()
    Post_Graduation=models.CharField(max_length=100)
    Post_Graduation_Stream=models.CharField(max_length=100)
    Post_Gradation_Passed_out_year=models.IntegerField()
    Trained_on_Technology=models.CharField(max_length=100)
    Where_did_you_trained_Institute_Name=models.CharField(max_length=100)
    Duration_of_Course=models.CharField(max_length=100)
    Reference_Name=models.CharField(max_length=50)
    Where_did_you_hear_about_the_interview=models.CharField(max_length=100)
    Experience=models.IntegerField()
    Previous_Company_Name=models.CharField(max_length=50)
    Current_CTC=models.BigIntegerField()
    Expected_CTC=models.BigIntegerField()
    Do_you_Have_PF_in_last_company=models.CharField(max_length=100)
    How_Many_years_of_Experience=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

class Rounds(models.Model):
    id=models.IntegerField(primary_key=True)
    marks_onlineTest=models.FloatField()
    isQualified_onlinetest=models.BooleanField()
    feedback_onlinetest=models.TextField(max_length=200)
    marks_communicationtest=models.FloatField()
    isQualified_communicationtest=models.BooleanField()
    feedback_communicationtest=models.TextField(max_length=200)
    marks_technicaltest=models.FloatField()
    isQualified_technicaltest=models.BooleanField()
    feedback_technicaltest=models.TextField(max_length=200)
    isSelected_ceoround=models.BooleanField()
    feedback_ceoround=models.TextField(max_length=200)
    aspirantsid=models.ForeignKey(Aspirant,on_delete=models.CASCADE)

class OnBoarded(models.Model):
    id=models.IntegerField(primary_key=True)
    isOnBoarded=models.BooleanField()
    aspirantsid=models.ForeignKey(Aspirant,on_delete=models.CASCADE)

    