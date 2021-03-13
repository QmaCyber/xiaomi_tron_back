from .models import Category, Product, PopularProduct, imagesSlider
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductsSerializer, PopularProductsSerializer, imagesSliderSerializer
from rest_framework.response import Response
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

class popularProductsView(APIView):
	def get(self, request, productSlug=''):
		Product = PopularProduct.objects.all()
		serializer = PopularProductsSerializer(Product, many=True)
		return Response({"popolarproducts": serializer.data})

class popularProductsView(APIView):
	def get(self, request):
		product = PopularProduct.objects.all()
		serializer = PopularProductsSerializer(Product, many=True)
		return Response({"popolarproducts": serializer.data})


class slider(APIView):
	def get(self, request):
		images = imagesSlider.objects.all()
		serializer =  imagesSliderSerializer(images, many=True)
		return Response({"images": serializer.data})
