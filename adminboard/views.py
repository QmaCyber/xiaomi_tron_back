from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth import authenticate
import json
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User


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
		products = Product.objects.all()
		foundProducts = []
		for product in products:
			if text.lower() in product.name.lower():
				foundProducts.append(product)
		serializer = ProductsSerializer(foundProducts, many=True)
		return Response({"products": serializer.data})


class SlidesView(APIView):
	def get(self, request):
		images = SliderImage.objects.all()
		serializer = ImagesSliderSerializer(images, many=True)
		return Response({"images": serializer.data})


class ReviewsView(APIView):
	def get(self, request):
		reviews = Review.objects.all()
		serializer = ReviewSerializer(reviews, many=True)
		return Response({"reviews": serializer.data})


class NewsView(APIView):
	def get(self, request):
		news = New.objects.all()
		serializer = NewSerializer(news, many=True)
		return Response({"News": serializer.data})
