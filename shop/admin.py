from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect

class CategoryAdmin(admin.ModelAdmin):
	def add_view(self, request):
		if request.method == 'POST':
			if Category.objects.count() > 12:
				return HttpResponseRedirect('NO')
		return super(CategoryAdmin, self).add_view(request)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(PopularProduct)
admin.site.register(ImagesSlider)
admin.site.register(News)