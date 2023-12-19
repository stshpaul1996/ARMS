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
    first_name = models.CharField(max_length=100, validators =(only_alp,))
    last_name = models.CharField(max_length=100,validators =(only_alp,))
    email_ID = models.EmailField(max_length = 100)
    phone_No = models.BigIntegerField()
    graduation = models.CharField(max_length =100, )
    stream = models.CharField(max_length =10,)
    grad_yop = models.IntegerField()
    post_graduation = models.CharField(max_length=100,)
    Pg_Stream = models.CharField(max_length=100,null= True, blank = True,)
    Pg_Passed_Out_Year = models.IntegerField(null= True, blank = True,)
    Trained_On_Technology = models.CharField(max_length=100)
    Institute_Name = models.CharField(max_length=250,validators =(only_alp,))
    Duration_of_course = models.IntegerField()
    Reference_Name = models.CharField(max_length=100,null= True, blank = True)
    hear_about_the_interview = models.CharField(max_length=250,validators =(only_alp,))
    Experience = models.IntegerField(null= True, blank = True)
    Previous_company_Name = models.CharField(max_length= 250,validators =(only_alp,))
    Current_CTC = models.IntegerField(null= True, blank = True,)
    Expected_CTC = models.IntegerField(null= True, blank = True,)
    PF_in_Last_Company = models.BigIntegerField(null= True, blank = True,)
    timestamp = models.DateTimeField(auto_now_add=True)
