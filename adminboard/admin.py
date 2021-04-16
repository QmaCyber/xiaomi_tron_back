from django.contrib import admin
from .models import *
from django.contrib.admin.widgets import AdminFileWidget

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PopularProduct)
admin.site.register(New)
admin.site.register(Review)
admin.site.register(SliderImage)
