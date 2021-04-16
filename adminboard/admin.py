from django.contrib import admin
from .models import *
from django.contrib.admin.widgets import AdminFileWidget
from sorl.thumbnail.admin import AdminImageMixin
		

admin.site.register(Category)
admin.site.register(PopularProduct)
admin.site.register(New)
admin.site.register(Review)
admin.site.register(SliderImage)

class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('name', 'category', 'description','available','available_ava','price', 'image_img')
	readonly_fields = ['image_img',]
	list_filter = ('available', 'created')
	search_fields = ('title', 'body')
	date_hierarchy = 'created'
	fields = ['category', 'name', 'image','description', 'price', 'stock']
	ordering = ['available', 'created']

admin.site.register(Product, ProductAdmin)