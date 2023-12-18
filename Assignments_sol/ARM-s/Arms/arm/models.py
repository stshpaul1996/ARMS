from django.core.exceptions import ValidationError
from django.db import models
from datetime import date
# Create your models here.
def phon_num(value):
    val=str(value)
    if len(val) != 10:
        raise ValidationError('the phone number should be ten numbers')
class Employee(models.Model):
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    date_of_join = models.DateField(default=date.today())
    poss = (('python', 'python'), ('java', 'java'), ('Reactjs', 'Reactjs'), ('.NET', '.NET'),
            ('Salesforce', 'Salesforce'), ('Devops', 'Devops'))
    technology_cat = models.CharField(max_length=100,choices=poss)
    poss = (('HR', 'HR'), ('Trainee software', 'Trainee software'), ('Finance manger', 'Finance manger'), ('Software engineer', 'Software engineer'),
            ('principil consultant', 'principil consultant'), ('manager', 'manager'))
    designation = models.CharField(max_length=250,choices=poss)
    poss=(('under training','under training'),('training completed','training completed'),('Deployed','Deployed'),('On bench','On bench'))
    employee_status = models.CharField(max_length=300,choices=poss)
    poss=(('Bsc','Bsc'),('Btech','Btech'),('AgBSc','AgBSc'),('BBA','BBA'),('Bcom','Bcom'),('BE','BE'),('BCA','BCA'))
    graduation = models.CharField(max_length=300,choices=poss)
    poss=(('computer science','computer science'),('mathematics','mathematics'),('science','science'),('data science','data science'),
          ('computer applications','computer applications'))
    stream = models.CharField(max_length=250,choices=poss)
    ug_year_of_passout = models.DateField()
    poss =(('Msc','Msc'),('MBA','MBA'),('Mtech','Mtech'),('ME','ME'),('MCA','MCA'))
    pg_education = models.CharField(max_length=250,choices=poss)
    pg_education_passout_year = models.DateField()
    poss =(('computer science','computer science'),('mathematics','mathematics'),('science','science'),('data science','data science'),
           ('computer applications','computer applications'),('civil engineering',"civil engineering"),('Finance',"Finance"),('IT','IT'))
    pg_stram = models.CharField(max_length=250,choices=poss)
    mobile_no = models.IntegerField(validators=[phon_num])
    alt_mobile_no = models.IntegerField(validators=[phon_num])
    remarks = models.CharField(max_length=250)
    def clean(self):
        if self.mobile_no == self.alt_mobile_no :
            raise ValidationError("should not give same numbers")

        # if self.ug_year_of_passout and self.pg_education_passout_year:
        #     years_difference = self.pg_education_passout_year.year - self.ug_year_of_passout.year
        #     if years_difference < 1:
        #         raise ValidationError("The difference between UG and PG pass-out years should be at least 1 year.")
        if self.ug_year_of_passout and self.pg_education_passout_year:
            days_difference = (self.pg_education_passout_year - self.ug_year_of_passout).days
            if days_difference < 365:
                raise ValidationError("The difference between UG and PG pass-out years should be at least 1 year.")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return ' --> '+self.first_name

class Pricipal_consultant(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    Consultant_name=models.CharField(max_length=50)
    clients=models.CharField(max_length=50)
    def __str__(self):
        return self.Consultant_name

class Deployed(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    date_of_deploy = models.DateField(default=date.today())
    designation = models.CharField(max_length=150)
    possibilities = (('contract based', 'contract based'), ('full time', 'full time'), ('off shore', 'off shore'))
    resource_type = models.CharField(max_length=250, choices=possibilities)
    client = models.CharField(max_length=150)
    project_start_date = models.DateField(default=date.today(), verbose_name=' Enter project start date')
    project_end_date = models.DateField(verbose_name='Enter project end date')
    possibilities=((True,'paid'),(False,'unpaid'))
    billstatus = models.BooleanField(choices=possibilities)
    bill_rate_per_month = models.IntegerField()
    candidate_ctc = models.IntegerField()
    possibilities = (('Hybrid Mode', 'Hybrid mode'), ('WTH', 'WTH'), ('WFO', 'WFO'))
    work_mode = models.CharField(max_length=200, choices=possibilities)
    poss = (('Hyderabad', 'hyderabad'), ('Bangolore', 'Bangolore'), ('chennai', 'chennai'), ('Mumbai', 'Mumbai'),
            ('Kochi', 'Kochi'), ('Delhi', 'Delhi'), ('Pune', 'Pune'), ('Kolkata', 'Kolkata'),
            ('Coimbatore', 'Coimbatore'), ('other', 'other'))
    work_location = models.CharField(max_length=200, choices=poss)
    # poss = (
    # ('Raghu', 'Raghu'), ('Ravi Teja', 'Ravi Teja'), ('Shiva', 'Shiva'), ('Vikram', 'Vikram'), ('Johnson', 'Johnson'))
    principil_consultent = models.ForeignKey(Pricipal_consultant,on_delete=models.CASCADE)
    remarks = models.TextField(max_length=300)
    def clean(self):
        if self.project_end_date <= self.project_start_date:
            raise ValidationError("The project_end_date should be in future of project_start_date")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.employee_id


class Employee_exit(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    date_of_exit = models.DateTimeField()
    exit_reason = models.CharField(max_length=250)

    def __str__(self):
        return self.employee_id

