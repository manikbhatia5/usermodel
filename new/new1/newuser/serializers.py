from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import * 

class userserializer (serializers.ModelSerializer):
    class Meta:
        model= usermodel
        fields = ('firstname', 'lastname','email','phone','id')

class employeeserializer (serializers.ModelSerializer):
    class Meta:
        model= employee
        fields = ('name','userId','id')

class userEmployeeJoin(serializers.ModelSerializer): 
    userId=userserializer()
    class Meta:
        model= employee
        fields = '__all__'