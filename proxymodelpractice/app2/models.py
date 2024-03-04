from django.db import models
from app.models import ParentModel

class Proxymodel(ParentModel):
    class Meta:
        proxy = True 

    
    # #import pdb;pdb.set_trace()
    # def age(self):
    #     original_age = super().age()  # Call the age() method of the ParentModel
    #     modified_age = original_age + 10
    #     return modified_age
