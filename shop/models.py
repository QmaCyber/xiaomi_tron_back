from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(default='')
	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(default='')
	image = models.ImageField(upload_to='images', blank=True)
	description = models.TextField(blank=True)
	price = models.PositiveIntegerField()
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	def __str__(self):
		return self.name


class PopularProduct(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(default='')
	image = models.ImageField(upload_to='images', blank=True)
	description = models.TextField(blank=True)
	oldprice = models.PositiveIntegerField()
	price = models.PositiveIntegerField()
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now = True)
	def __str__(self):
		return self.name

class ImageSliderColors(models.Model):
	color = models.CharField(max_length=50)
	def __str__(self):
		return self.color

class ImagesSlider(models.Model):
	colors = models.ForeignKey(ImageSliderColors, related_name='colors', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='images', blank=False)
	def __str__(self):
		return self.name

class News(models.Model):
	name = models.CharField(max_length=30, db_index=True)
	slug = models.SlugField(blank=False, default='')
	image = models.ImageField(upload_to='images', blank=True)
	information = models.TextField(max_length=1000, blank=False)

	def __str__(self):
		return self.name


class Review(models.Model):
	name = models.CharField(max_length=30, db_index=True)
	slug = models.SlugField(default='')
	reviewUrl = models.URLField(max_length=254)