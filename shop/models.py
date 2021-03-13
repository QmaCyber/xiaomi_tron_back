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
