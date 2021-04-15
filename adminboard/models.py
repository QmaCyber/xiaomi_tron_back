from django.db import models
from autoslug import AutoSlugField



class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = AutoSlugField(populate_from='name')

	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(
		Category, related_name='products', on_delete=models.CASCADE)
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
	price = models.PositiveIntegerField()
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class SliderImage(models.Model):
	BLACK = 'BLACK'
	WHITE = 'WHITE'
	COLOR_CHOICES = (
		(BLACK, 'black'),
		(WHITE, 'white'),
	)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	color_text = models.CharField(max_length=10, choices=COLOR_CHOICES, default=BLACK)
	name = models.CharField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='images', blank=False)

	def __str__(self):
		return self.name


class New(models.Model):
	title = models.CharField(max_length=70, db_index=True)
	shortDescription = models.TextField(max_length=300, blank=True)
	image = models.ImageField(upload_to='images', blank=True)
	url = models.URLField(max_length=250, default="")
	created = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
	description = models.TextField(blank=True)
	content = models.TextField(blank=True)
=======
>>>>>>> 3ca6c58c795d5a056c207ba48db833a61352ba42

	def __str__(self):
		return self.title

<<<<<<< HEAD

class Review(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	video = models.URLField(max_length=250)
=======
class Review(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	video = models.URLField(max_length=250, default='')
	def __str__(self):
		return self.name
>>>>>>> 3ca6c58c795d5a056c207ba48db833a61352ba42

	def __str__(self):
		return self.name
