from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator

# Create your models here.
def only_alp(value):
    if not value.isalpha():
        raise ValidationError('Enter only alphabets only')

def get_next_application_no():
        last_aspirant = Aspirant.objects.order_by('-application_no').first()
        if last_aspirant is not None:
            return last_aspirant.application_no + 1
        return 100

LANGUAGE_CHOICES = [
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('DotNet', 'DotNET'),
    ('Salesforce', 'Salesforce'),
    ('ReactJS', 'ReactJS'),
    ('DevOps', 'DevOps'),
]

class Aspirant(models.Model):
    application_no = models.BigIntegerField(default=get_next_application_no,)
    first_name = models.CharField(max_length=100, validators =(only_alp,),verbose_name= 'First Name')
    last_name = models.CharField(max_length=100,validators =(only_alp,), verbose_name = 'Last Name')
    email_ID = models.EmailField(max_length = 100, verbose_name= 'Email')
    phone_No = models.BigIntegerField(verbose_name='Phone Number')
    graduation = models.CharField(max_length =100,verbose_name='Graduation' )
    stream = models.CharField(max_length =10,verbose_name= 'Stream')
    grad_yop = models.IntegerField(verbose_name= 'Graduation year of pass')
    post_graduation = models.CharField(max_length=100,verbose_name= 'Post Graduation')
    pg_Stream = models.CharField(max_length=100,null= True, blank = True,verbose_name= 'Post Graduation Stream')
    pg_Passed_Out_Year = models.IntegerField(null= True, blank = True, verbose_name= 'Post Graduation Year of Pass')
    trained_On_Technology = models.CharField(max_length=100,choices=LANGUAGE_CHOICES,verbose_name='Technology Trained On')
    institute_Name = models.CharField(max_length=250,validators =(only_alp,), verbose_name= 'Name of the Institute where you Trained')
    duration_of_course = models.IntegerField(verbose_name= 'Course Duration')
    reference_Name = models.CharField(max_length=100,null= True, blank = True, verbose_name='Reference Name')
    hear_about_the_interview = models.CharField(max_length=250,validators =(only_alp,),verbose_name='Where did you heard about the interview?')
    experience = models.IntegerField(null= True, blank = True,verbose_name= 'Experience')
    previous_company_Name = models.CharField(max_length= 250,validators =(only_alp,),verbose_name='Name of Previous Company Name')
    current_CTC = models.IntegerField(null= True, blank = True,verbose_name='Current CTC')
    expected_CTC = models.IntegerField(null= True, blank = True,verbose_name='Expect CTC')
    pf_in_Last_Company = models.BooleanField(null= True, blank = True,verbose_name='Do you have PF')
    timestamp = models.DateTimeField(auto_now_add=True)

class Rounds(models.Model):
    marks_communication_test = models.IntegerField(verbose_name='Marks',null = True, validators=[MaxValueValidator(limit_value=10)])
    isQualified_communication_test = models.BooleanField(verbose_name='Qualified',null = True)
    feedback_communication_test = models.TextField(verbose_name='Feedback')
    marks_technical_test = models.IntegerField(verbose_name='Marks', null = True,validators=[MaxValueValidator(limit_value=10)])
    isQualified_technical_test = models.BooleanField(verbose_name='Qualified', null = True)
    feedback_technical_test = models.TextField(verbose_name='Marks', null = True)
    marks_CEO_test = models.IntegerField(verbose_name='Marks', null = True,validators=[MaxValueValidator(limit_value=10)])
    isQualified_CEO_test = models.BooleanField(verbose_name='Selected ', null = True)
    feedback_CEO_test = models.TextField(verbose_name='Marks', null = True)
    aspirantid = models.ForeignKey(Aspirant, on_delete=models.PROTECT)

class OnBoarded(models.Model):
    isonboared = models.BooleanField(verbose_name='On Boarded or Not On Boarded',null = True)
    aspirantid = models.ForeignKey(Aspirant, on_delete=models.PROTECT)





