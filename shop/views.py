from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth import authenticate
import json


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

class PopularProductsView(APIView):
	def get(self, request, productSlug=''):
		Product = PopularProduct.objects.all()
		serializer = PopularProductsSerializer(Product, many=True)
		return Response({"popolarproducts": serializer.data})
	
class SearchView(APIView):
	def get(self, request, text):
		products = Product.objects.all()
		foundProducts = []
		for product in products:
			if text.lower() in product.name.lower():
				foundProducts.append(product)
		serializer = ProductsSerializer(foundProducts, many=True)
		return Response({"products":serializer.data})


class SlidersView(APIView):
	def get(self, request):
		images = imagesSlider.objects.all()
		serializer = ImagesSliderSerializer(images, many=True)
		return Response({"images": serializer.data})

class LoginView(APIView):
	def post(self, request):
		loginpassword=json.loads(request.body)
		login = loginpassword.get('login')
		password = loginpassword.get('password')
		print(login, password)
		request.session['token']='231321'
		print(request.session['token'])
		user = authenticate(username=login, password=password)
		if user is not None:
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=201)

class NewsView(APIView):
	def get(self, request, newsSlug=''):
		if newsSlug =='':
			news = News.objects.all()
			serializer = NewsSerializer(news, many=True)
			return Response({"News": serializer.data})
		else:
			news = News.objects.get(slug=newsSlug)
			serializer = NewsSerializer(news, many=False)
			return Response({"News": serializer.data})
