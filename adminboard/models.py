from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = AutoSlugField(populate_from='name')
	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	slug = AutoSlugField(populate_from='name')
	image = models.ImageField(upload_to='images', blank=True)
	description = models.TextField(blank=True)
	price = models.PositiveIntegerField()
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name


class PopularProduct(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = AutoSlugField(populate_from='name')
	image = models.ImageField(upload_to='images', blank=True)
	description = models.TextField(blank=True)
	oldprice = models.PositiveIntegerField()
	newprice = models.PositiveIntegerField()
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

class New(models.Model):
	title = models.CharField(max_length=70, db_index=True)
	shortDescription = models.TextField(max_length=300, blank=True)
	image = models.ImageField(upload_to='images', blank=True)
	url = models.URLField(max_length=250, default="")
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Review(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	video = models.URLField(max_length=250, default='')
	def __str__(self):
		return self.name

class SliderImage(models.Model):
	BLACK = 'BLACK'
	WHITE = 'WHITE'
	COLOR_CHOICES = (
		(BLACK, 'black'),
		(WHITE, 'white'),
	)
	color_text = models.CharField(max_length=10, choices=COLOR_CHOICES, default=BLACK)
	name = models.CharField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='images', blank=False)
	def __str__(self):
		return self.name
