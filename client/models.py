from django.db import models
from django.contrib.auth.models import User
from adminboard.models import *


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete  = models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	adress =  models.CharField(max_length=200, db_index=True,null=True)
	phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='phone')
	def __str__(self):
		return self.phone

class Cart(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

class History(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
