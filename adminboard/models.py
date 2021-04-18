from django.db import models
from autoslug import AutoSlugField
from django.utils.safestring import mark_safe


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
	created = models.DateTimeField(auto_now_add=True)
	def image_img(self):
		if self.image:
			return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(self.image.url))
		else:
			return 'No image'
	image_img.short_description = 'Image'
	image_img.allow_tags = True
	
	def available_ava(self):
		if self.stock == 0:
			return False
		else:
			return True
	available_ava.short_description = 'available'

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
	def image_img(self):
		if self.image:
			return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(self.image.url))
		else:
			return 'No image'
	image_img.short_description = 'Image'
	image_img.allow_tags = True
	
	def available_ava(self):
		if self.stock == 0:
			return False
		else:
			return True
	available_ava.short_description = 'available'

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
	name = models.CharField(max_length=30, db_index=True)
	title = models.CharField(max_length=70)
	slug = AutoSlugField(populate_from='name')
	image = models.ImageField(upload_to='images', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	description = models.TextField(blank=True)
	content = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Review(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	video = models.URLField(max_length=250)

	def __str__(self):
		return self.name
