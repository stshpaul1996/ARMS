from django.db import models

# Create your models here.
class Aspirant(models.Model):
    application_no = models.IntegerField(null=True,verbose_name='Appliation_Number')
    full_name = models.CharField(max_length=50,null=True,verbose_name='Full Name')
    email = models.EmailField(max_length=50,null=True,verbose_name='Email_ID')
    phone_no = models.CharField(max_length=13,null=True,verbose_name='Phone Number')
    gradution = models.CharField(max_length=50,null=True,verbose_name='Gradution')
    post_gradution = models.CharField(max_length=50,null=True,verbose_name='Post Gradution')
    stream = models.CharField(max_length=50,null=True,verbose_name='Stream')
    passed_out_year=models.IntegerField(null=True,verbose_name='Passed out year')
    trained_on_technology = models.CharField(max_length=50,null=True,verbose_name='Trained on Technology')
    trained_institue = models.CharField(max_length=50,null=True,verbose_name='Where did you trained institue name')
    duration_of_course = models.CharField(max_length=50,null=True,verbose_name='Duration of course')
    reference_name = models.CharField(max_length=25,null=True,verbose_name='Refernce Name')
    hear_about_interview = models.CharField(max_length=50,null=True,verbose_name='Where did you hear about the interview')
    experience = models.CharField(max_length=25,null=True,verbose_name='Experience')
    Previous_company_name = models.CharField(max_length=50,null=True,verbose_name='Previous Company Name')
    current_ctc = models.CharField(max_length=50,null=True,verbose_name='Current_CTC')
    expected_ctc = models.CharField(max_length=50,null=True,verbose_name='Expected_CTC')
    last_company = models.CharField(max_length=50,null=True,verbose_name='Do you have PF in last company')
    years_of_experience = models.CharField(max_length=50,null=True,verbose_name='How many year of experice')
    created_at = models.DateField(null=True,verbose_name='Created at')

class Rounds(models.Model):
    marks_onlinetest=models.FloatField(max_length=25,null=True)
    isQualified_online=models.BooleanField(default=False)
    feedback_online=models.TextField(max_length=58)
    marks_communication_test = models.FloatField(max_length=25)
    isQualified_comm=models.BooleanField(default=False)
    feedback_comm=models.TextField(max_length=52)
    marks_technicaltest = models.FloatField(max_length=22)
    isQualified_test=models.BooleanField(default=False)
    feedback_technical=models.TextField(max_length=52)
    isselected = models.BooleanField(default=False)
    feedback=models.TextField(max_length=250)
    aspirantsid=models.ForeignKey(Aspirant,on_delete=models.CASCADE)

class Onboared(models.Model):
    Onboarded=models.BooleanField(default=False)
    Aspirantid=models.ForeignKey(Aspirant,on_delete=models.CASCADE)