from .models import Category, Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductsSerializer
from rest_framework.response import Response
from .models import Product

class ProductsView(APIView):
	def get(self, request, categorySlug=''):
		if categorySlug=='':
			Products = Product.objects.all()
			serializer = ProductsSerializer(Products, many=True)
			return Response({"products": serializer.data})
		else: 
			_category = Category.objects.get(slug=categorySlug)
			categoryProducts = Product.objects.filter(category=_category)
			serializer = ProductsSerializer(categoryProducts, many=True)
			return Response({"products": serializer.data})
class ProductView(APIView):
	def get(self, request, productSlug=''):
		product = Product.objects.get(slug=productSlug)
		serializer = ProductsSerializer(product, many=False)
		return Response({"product":serializer.data})