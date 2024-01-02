from django.db import models
from django.core.exceptions import ValidationError



# Create your models here.
def only_alp(value):
    if not value.isalpha():
        raise ValidationError('Enter only alphabets only')

def get_next_application_no():
        last_aspirant = Aspirant.objects.order_by('-application_no').first()
        if last_aspirant is not None:
            return last_aspirant.application_no + 1
        return 100

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
    Pg_Stream = models.CharField(max_length=100,null= True, blank = True,verbose_name= 'Post Graduation Stream')
    Pg_Passed_Out_Year = models.IntegerField(null= True, blank = True, verbose_name= 'Post Graduation Year of Pass')
    Trained_On_Technology = models.CharField(max_length=100,verbose_name='Technology Trained On')
    Institute_Name = models.CharField(max_length=250,validators =(only_alp,), verbose_name= 'Name of the Institute where you Trained')
    Duration_of_course = models.IntegerField(verbose_name= 'Course Duration')
    Reference_Name = models.CharField(max_length=100,null= True, blank = True, verbose_name='Reference Name')
    hear_about_the_interview = models.CharField(max_length=250,validators =(only_alp,),verbose_name='Where did you heard about the interview?')
    Experience = models.IntegerField(null= True, blank = True,verbose_name= 'Experience')
    Previous_company_Name = models.CharField(max_length= 250,validators =(only_alp,),verbose_name='Name of Previous Company Name')
    Current_CTC = models.IntegerField(null= True, blank = True,verbose_name='Current CTC')
    Expected_CTC = models.IntegerField(null= True, blank = True,verbose_name='Expect CTC')
    PF_in_Last_Company = models.BooleanField(null= True, blank = True,verbose_name='Do you have PF')
    timestamp = models.DateTimeField(auto_now_add=True)
