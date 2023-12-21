from django import forms
from .models import Employee,Daily_Atendance
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_slug

from  datetime import time,timedelta,datetime

def validate_phoneNum(number):
    if len(str(number)) <10:
        raise ValidationError("enter 10 digits " )


class EmployeeForm(forms.Form):
    email_id = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=50)
    validate_phone_number = forms.IntegerField(validators=[validate_phoneNum])
    address = forms.CharField(max_length=250,validators=[validate_slug])
    tech_id = forms.IntegerField()

class DailyAttendanceForm(forms.Form):
    employee_id = forms.ModelChoiceField(queryset=Employee.objects.all())

    date = forms.DateField()
    check_in = forms.TimeField()
    check_out = forms.TimeField()

    def calculate_time_diff(self,check_in,check_out):

        time1 = check_in.hour * 3600 + check_in.minute * 60 + check_in.second 
        time2 = check_out.hour * 3600 + check_out.minute * 60 + check_out.second 

        time_diff_seconds = abs(time2 - time1)
        return timedelta(seconds = time_diff_seconds)

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        if check_in and check_out:

            time_diff = self.calculate_time_diff(check_in,check_out)
            if time_diff < timedelta(hours=9):
                cleaned_data['status'] = "A"
            else:
                cleaned_data['status'] = "P"
        
        return cleaned_data

