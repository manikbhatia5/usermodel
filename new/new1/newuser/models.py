
from pickle import FALSE
from unicodedata import name
from django.db import models

# Create your models here.

class usermodel(models.Model):
	id=models.AutoField(primary_key=True)
	firstname=models.CharField(max_length=122,null=True)
	lastname=models.CharField(max_length=122,null=True)
	email=models.CharField(max_length=40,null=True)
	phone=models.CharField(max_length=12,null=True)
    
	def __str__(self):
	     return self.firstname


class employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=True)
    userId = models.ForeignKey(usermodel,on_delete=models.SET_NULL,null=True,blank=False)

    def __str__(self):
        return self.name

