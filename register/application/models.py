from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Aspirant(models.Model):
    F_name=models.CharField(max_length=100,null=True,verbose_name='First name')
    L_name=models.CharField(max_length=100,null=True,verbose_name='Last name')
    Email_id=models.EmailField(max_length=100,null=True)
    Phone_no=models.IntegerField(null=True,help_text="Enter your phone number")
    Graduation_choices=[
        ("btech","B.Tech"),
        ("bsc","B.Sc"),
        ("ba","B.A"),
        ("bcom","B.Com"),
        ("degree","Degree")
    ]
    Graduation=models.CharField(max_length=10,null=True,choices=Graduation_choices)
    Graduation_Stream=models.CharField(null=True,max_length=100)
    Graduation_Passed_Out_Year=models.IntegerField(null=True,help_text="passed out year should be >2016 and <2023")
    Post_Graduation_choices=[
        ("mtech","M.Tech"),
        ("mba","MBA"),
        ("mca","MCA"),
        ("mcom","M.COM"),
        ("msc","M.SC")
    ]
    Post_Graduation=models.CharField(max_length=10,choices=Post_Graduation_choices)
    Post_Graduation_Stream=models.CharField(max_length=100)
    Post_Gradation_Passed_out_year=models.IntegerField(null=True,help_text="passed out year should be >2016 and <2023")
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
    Duration_of_Course=models.CharField(null=True,max_length=100)
    Reference_Name=models.CharField(null=False,max_length=50)
    Where_did_you_hear_about_the_interview=models.CharField(null=True,max_length=100)
    Experienc_choices=(
                ("yes","yes"),
                ("no","no"))
    Experience=models.CharField(max_length=10,choices=Experienc_choices)
    Previous_Company_Name=models.CharField(null=True,max_length=50)
    Current_CTC=models.BigIntegerField(null=True)
    Expected_CTC=models.BigIntegerField(null=True)
    PF_choices=(
            ("yes","yes"),
            ("no","no"))
    Do_you_Have_PF_in_last_company=models.CharField(null=True,max_length=100,choices=PF_choices)
    How_Many_years_of_Experience=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        errors={}
        if len(str(self.Phone_no))<10:
            errors["Phone_no"]=ValidationError("Phone number should contain at least 10 characters")
            
        if len(self.F_name)<=3:
            errors["F_name"]=ValidationError("First name should be more than 3 characters")

        if len(self.L_name)<=3:
            errors["L_name"]=ValidationError("Last name should be more than 3 characters")

        if not self.Email_id.endswith("@gmail.com"):
            errors["Email_id"]=ValidationError("email id should be gmail only")

        if not (2016 <self.Graduation_Passed_Out_Year <2023):
            errors["Graduation_Passed_Out_Year"]=ValidationError("Graduation_Passed_Out_Year shoud be greater than 2016 and less than 2023")

        if errors:
            raise ValidationError(errors)
# class Rounds(models.Model):
#     marks_onlineTest=models.FloatField()
#     isQualified_onlinetest=models.BooleanField()
#     feedback_onlinetest=models.TextField(max_length=200)
#     marks_communicationtest=models.FloatField()
#     isQualified_communicationtest=models.BooleanField()
#     feedback_communicationtest=models.TextField(max_length=200)
#     marks_technicaltest=models.FloatField()
#     isQualified_technicaltest=models.BooleanField()
#     feedback_technicaltest=models.TextField(max_length=200)
#     isSelected_ceoround=models.BooleanField()
#     feedback_ceoround=models.TextField(max_length=200)
#     aspirantsid=models.ForeignKey(Aspirant,on_delete=models.PROTECT)

# class OnBoarded(models.Model):
#     isOnBoarded=models.BooleanField()
#     aspirantsid=models.ForeignKey(Aspirant,on_delete=models.PROTECT)


    