from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def fullname(value):
    if len(str(value))<3 or not value.isupper():
        raise ValidationError('name should be not lessthan 3 and should be capital letter')
    
def emailid(value):
        if not value.endswith("@gmail.com"):
            raise ValidationError("email should be @gmail.com only")
        
def gradutionyear(value):
        if not (2016 <= value <=2023) or len(str(value))!=4:
            raise ValidationError("passed out year should be greater than 2016 and lessthan 2023 and should be 4 digits")

def moblie(value):
     if len(str(value))<=9 or not value or not value.startswith(('6', '7', '8', '9')):
          raise ValidationError('Enter valid phone number')

gradutionchoices=(('B.Tech','B.Tech'),('Bcom','Bcom'),('M.Tech','M.Tech'),('BE','BE'),('BCA','BCA'),('MBA','MBA'),('MCA','MCA'),
           ('MSc','MSc'),('MA','MA'),('B Sc','B Sc'))
technologychoices=(('Python','Python'),('Java','Java'),('DotNet','DotNet'),('Devops','Devops'),('Testing','Testing'),
                  ('Salesforce','Salesforce'),('ReactJS','ReactJS'),('DataScience','DataScience'))

experiencechoices=(('YES','YES'),('NO','NO'))

class Aspirant(models.Model):
    full_name = models.CharField(max_length=50,null=True,verbose_name='Full Name',validators=(fullname,))
    email = models.EmailField(max_length=50,null=True,verbose_name='Email_ID',validators=(emailid,))
    phone_no = models.CharField(max_length=13,null=True,unique=True,verbose_name='Phone Number',
                                validators=(moblie,))
    gradution = models.CharField(max_length=50,null=True,verbose_name='Gradution',
                                 choices=(gradutionchoices))
    post_gradution = models.CharField(max_length=50,null=True,verbose_name='Post Gradution')
    stream = models.CharField(max_length=50,null=True,verbose_name='Stream')
    passed_out_year=models.IntegerField(null=True,verbose_name='Passed out year',validators=(gradutionyear,))
    trained_on_technology = models.CharField(max_length=50,null=True,verbose_name='Trained on Technology',choices=technologychoices)
    trained_institue = models.CharField(max_length=50,null=True,verbose_name='Where did you trained institue name')
    duration_of_course = models.CharField(max_length=50,null=True,verbose_name='Duration of course')
    reference_name = models.CharField(max_length=25,null=True,verbose_name='Refernce Name')
    hear_about_interview = models.CharField(max_length=50,null=True,verbose_name='Where did you hear about the interview')
    experience = models.CharField(max_length=25,null=True,verbose_name='Experience',choices=experiencechoices)
    Previous_company_name = models.CharField(max_length=50,null=True,verbose_name='Previous Company Name')
    current_ctc = models.CharField(max_length=50,null=True,verbose_name='Current_CTC')
    expected_ctc = models.CharField(max_length=50,null=True,verbose_name='Expected_CTC')
    last_company = models.CharField(max_length=50,null=True,verbose_name='Do you have PF in last company')
    years_of_experience = models.CharField(max_length=50,null=True,verbose_name='How many year of experice')
    created_at = models.DateTimeField(null=True,verbose_name='Created at',auto_now_add=True)

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
    aspirantsid=models.ForeignKey(Aspirant,on_delete=models.PROTECT)

class Onboared(models.Model):
    Onboarded=models.BooleanField(default=False)
    Aspirantid=models.ForeignKey(Aspirant,on_delete=models.PROTECT)