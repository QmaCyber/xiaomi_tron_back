import json

from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User


from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class ProductsView(APIView):
	def get(self, request):
		Products = Product.objects.all()
		serializer = ProductsSerializer(Products, many=True)
		return Response({"products": serializer.data})


class ProductCategoryView(APIView):
	def get(self, request, categorySlug=''):
		_category = Category.objects.get(slug=categorySlug)
		categoryProducts = Product.objects.filter(category=_category)
		serializer = ProductsSerializer(categoryProducts, many=True)
		return Response({"products": serializer.data})


class CategoryView(APIView):
	def get(self, request):
		categorys = Category.objects.all()
		serializer = CategorySerializer(categorys, many=True)
		return Response({'categorys': serializer.data})


class ProductView(APIView):
	def get(self, request, productSlug=''):
		product = Product.objects.get(slug=productSlug)
		if product.stock == 0:
			product.available = False
			product.save()
		serializer = ProductsSerializer(product, many=False)
		return Response({"product": serializer.data})


class PopularProductsView(APIView):
	def get(self, request, productSlug=''):
		Product = PopularProduct.objects.all()
		serializer = PopularProductsSerializer(Product, many=True)
		return Response({"popolarproducts": serializer.data})


class SearchView(APIView):
	def get(self, request, text):
		products1 = PopularProduct.objects.all() 
		products2 = Product.objects.all()
		foundProducts = []
		for product in products1:
			if text.lower() in product.name.lower():
				foundProducts.append(product)
		for product in products2:
			if text.lower() in product.name.lower():
				foundProducts.append(product)
		return Response({"products":serializer.data})


class SlidersView(APIView):
	def get(self, request):
		images = ImagesSlider.objects.all()
		serializer = ImagesSliderSerializer(images, many=True)
		return Response({"images": serializer.data})


class ReviewsView(APIView):
	def get(self, request):
		reviews = Review.objects.all()
		serializer = ReviewSerializer(reviews, many=True)
		return Response({"reviews": serializer.data})


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


class LoginView(APIView):
	def post(self, request):
		loginpassword=json.loads(request.body)
		login = loginpassword.get('login')
		password = loginpassword.get('password')
		user = authenticate(username=login, password=password)
		if user is not None:
			token = Token.objects.create(user=user)
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=201)


class ResiterView(APIView):
	def post(self, request):
		loginpassword=json.loads(request.body)
		login = loginpassword.get('login')
		password = loginpassword.get('password')
		try:
			userLog = User.objects.get(username=login)
		except User.DoesNotExist:
			userLog = True
		else:
			userLog = False
		
		if userLog:
			user = User.objects.create_user(username=login,
											password=password)
			return HttpResponse(status=200)	
		else:
			return HttpResponse(status = 201)


class AuthMeView(APIView):
	def post(self, request, token = ''):
		tokens = Token.objects.all()
		if token in tokens:
			return HttpResponse(status=200)
		else:
			return HttpResponse(status = 201)