from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)

    class Meta:
        model = Country
        fields = '__all__'

    def create(self, validated_data):
        country_obj = Country(**validated_data)
        country_obj.save()
        return country_obj


    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = employee
        #fields = ('fname', 'lname',) comment it becouse we need all data
        fields = '__all__'  # use to get whole data
