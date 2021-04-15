from django.db import models
from django.contrib.auth.models import User
from adminboard.models import *



class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	adress =  models.CharField(max_length=200, db_index=True,null=True)

class Cart(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

class History(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

