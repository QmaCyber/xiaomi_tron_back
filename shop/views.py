from .models import Category, Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductsSerializer
from rest_framework.response import Response
from .models import Product
from django.http import HttpResponse

class ProductsView(APIView):
	def get(self, request):
		Products = Product.objects.all()
		serializer = ProductsSerializer(Products, many=True)
		return Response({"products": serializer.data})
		
class CategoryView(APIView):
	def get(self, request, categorySlug=''):
		_category = Category.objects.get(slug=categorySlug)
		categoryProducts = Product.objects.filter(category=_category)
		serializer = ProductsSerializer(categoryProducts, many=True)
		return Response({"products": serializer.data})

class ProductView(APIView):
	def get(self, request, productSlug=''):
		product = Product.objects.get(slug=productSlug)
		if product.stock == 0:
			product.available = False 
			product.save()
		serializer = ProductsSerializer(product, many=False)
		return Response({"product":serializer.data})
