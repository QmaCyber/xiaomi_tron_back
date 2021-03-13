from django.contrib import admin
from .models import Category, Product, PopularProduct, imagesSlider


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PopularProduct)
admin.site.register(imagesSlider)