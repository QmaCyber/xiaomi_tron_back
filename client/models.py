from django.db import models
from django.conf import settings
from adminboard.models import *

class Profile(models.Model):
	pass

class Comment(models.Model):
	user = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
	text = models.TextField(blank=True)
	rating = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
	pass