from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PopularProduct)
admin.site.register(New)
admin.site.register(Rewiew)
admin.site.register(SliderImage)