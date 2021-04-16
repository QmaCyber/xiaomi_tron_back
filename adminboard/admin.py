from django.contrib import admin
from .models import *
from django.contrib.admin.widgets import AdminFileWidget
from sorl.thumbnail.admin import AdminImageMixin
		

admin.site.register(Category)

admin.site.register(New)
admin.site.register(Review)
admin.site.register(SliderImage)

class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('name','stock', 'category', 'description','available_ava','price','image_img')
	readonly_fields = ['image_img', 'available_ava']
	list_filter = ('created',)
	search_fields = ('title', 'body')
	date_hierarchy = 'created'
	fields = ['category', 'name', 'image','description', 'price', 'stock']
	ordering = ['created']

class PopularProductAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('name','stock', 'description','available_ava', 'oldprice','price','image_img')
	readonly_fields = ['image_img', 'available_ava']
	list_filter = ('created',)
	search_fields = ('title', 'body')
	date_hierarchy = 'created'
	fields = ['name', 'image','description','oldprice', 'price', 'stock']

admin.site.register(Product, ProductAdmin)
admin.site.register(PopularProduct, PopularProductAdmin)