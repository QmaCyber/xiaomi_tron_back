from django.contrib import admin
from .models import Category, Product, PopularProduct


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PopularProduct)