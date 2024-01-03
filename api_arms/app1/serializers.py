from rest_framework import serializers 
from app1.models import Person
from django.core.exceptions import ValidationError

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def validate_name(self, value=None):
        if value.isalnum():
            return value.upper()
            #return value
        raise ValidationError("exepcting alpha numneric value.")
    
    def validate(self, *args, **kwargs):
        #self.validated_data = super(PersonSerializer, self).validate(*args)
        # import pdb;pdb.set_trace()
        
        data = self.initial_data
        age = data.get("age")
        if age and age>=18:
            if not data.get("email"):
                raise ValidationError("Email mandatory")
        return super(PersonSerializer, self).validate(*args)

           

    # def clean_name(self, value=None):
    #     import pdb;pdb.set_trace()
    #     print("hello")

    
