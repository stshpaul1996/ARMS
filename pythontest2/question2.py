# Write two best scenarios where inheritance can be used. Note:  don’t simply say that  we can call parent class methods and attributes.

# scenario 1:

from django.contrib.auth.models import models
from app1.models import customer
from django.core.exceptions import ValidationError
class New_customer(customer):
    phone_phone = models.IntegerField()
    email = models.EmailField()

# In the above example i have name,address fields in one model in one application i created 
# another application but i want to use model which is their in one application so, in this case we case inheritance
# concept i inherited customermodel from app1 application i created another fields 




# scenario  2:

class Product(models.model):
    name = models.CharField()
    unique_id = models.IntegerField()

class sales(Product):
    sales = models.IntegerField()

class Purchase(Product):
    purchase = models.IntegerField()


# In the above scenario i created one model Product and i want to check how many number of products i sold and purchadsed so for this requird all fields
# so i inherited Productclass in sales and purchse .

