from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def name(value):
    if len(value)<3:
        raise ValidationError("name should be more than 3 characters")
    
def email(value):
    if not value.endswith("@gmail.com"):
        raise ValidationError("mail id should be gmail")
    
def phone_no(value):
    if len(str(value))<10:
        raise ValidationError("phone number should contain at least 10 characters")
    
def alpha_numeric(value):
    if not value.isalnum():
        raise ValidationError("Expecting alphanumeric values")
    
def passout_year(value):
    if not (2016 < value < 2023):
        raise ValidationError('Passed out year should be greater than 2016 and less than 2023')


class Aspirant(models.Model):
    F_name=models.CharField(max_length=100,null=True,verbose_name='First name',validators=[name])
    L_name=models.CharField(max_length=100,null=True,verbose_name='Last name',validators=[name])
    Email_id=models.EmailField(max_length=100,null=True,validators=[email])
    Phone_no=models.IntegerField(null=True,help_text="Enter your phone number",validators=[phone_no])
    Graduation_choices=[
        ("btech","B.Tech"),
        ("bsc","B.Sc"),
        ("ba","B.A"),
        ("bcom","B.Com"),
        ("degree","Degree")
    ]
    Graduation=models.CharField(max_length=10,null=True,choices=Graduation_choices)
    Graduation_Stream=models.CharField(null=True,max_length=100)
    Graduation_Passed_Out_Year=models.IntegerField(null=True,help_text="passed out year should be >2016 and <2023",validators=[passout_year])
    Post_Graduation_choices=[
        ("mtech","M.Tech"),
        ("mba","MBA"),
        ("mca","MCA"),
        ("mcom","M.COM"),
        ("msc","M.SC")
    ]
    Post_Graduation=models.CharField(max_length=10,choices=Post_Graduation_choices)
    Post_Graduation_Stream=models.CharField(max_length=100)
    Post_Gradation_Passed_out_year=models.IntegerField(null=True,validators=[passout_year])
    Technology_choices=[
        ("python","Python"),
        ("java","JAVA"),
        (".net",".NET"),
        ("reactjs","ReactJS"),
        ("salesforce","Salesforce"),
        ("devops","Devops"),
    ]
    Trained_on_Technology=models.CharField(max_length=10,null=True,choices=Technology_choices)
    Where_did_you_trained_Institute_Name=models.CharField(null=True,max_length=100)
    Duration_of_Course=models.CharField(null=True,max_length=100,validators=[alpha_numeric])
    Reference_Name=models.CharField(null=False,max_length=50)
    Where_did_you_hear_about_the_interview=models.CharField(null=True,max_length=100)
    Experience_choices=(
                ("yes","yes"),
                ("no","no"))
    Experience=models.CharField(max_length=10,choices=Experience_choices)
    Previous_Company_Name=models.CharField(null=True,max_length=50)
    Current_CTC=models.BigIntegerField(null=True)
    Expected_CTC=models.BigIntegerField(null=True)
    Pf_choices=(
                ("yes","yes"),
                ("no","no"))
    Do_you_Have_PF_in_last_company=models.CharField(null=True,max_length=100,choices=Pf_choices)
    How_Many_years_of_Experience=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)