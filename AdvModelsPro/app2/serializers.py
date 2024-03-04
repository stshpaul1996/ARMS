from rest_framework import serializers
from .models import ProxyUserProfile, Visits

class ProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProxyUserProfile
        fields = ["username", "pancard"]

        def retrieve(self,value):
            un = value.get("username")
            value["username"] = "MRS"+ un


class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = "__all__"
    

    