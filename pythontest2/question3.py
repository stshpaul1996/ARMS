# Consider that you got a django application (customer) in github, that can be used in your project. 

# It has Customer model fields(name, address). the existing Customer model will not verify for special symbols of customer name field.
# Use Customer model and provide name validation for special symbols and add phone and email fields. 
from django.contrib.auth.models import models
from app1.models import customer
from django.core.exceptions import ValidationError
class New_customer(customer):
    phone_phone = models.IntegerField()
    email = models.EmailField()

    def validate(self,validated_data):
        validated_data = super().validate()
        name = validated_data.get('name')
        if not name.isalpha():
            raise ValidationError("name contains special symbols")
        return name