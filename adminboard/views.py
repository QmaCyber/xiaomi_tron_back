import json

from .models import *
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User
from client.models import *

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
		serializer = ProductsSerializer(product, many=False)
		return Response({"product": serializer.data})


class PopularProductsView(APIView):
	def get(self, request, productSlug=''):
		Product = PopularProduct.objects.all()
		serializer = PopularProductsSerializer(Product, many=True)
		return Response({"popolarproducts": serializer.data})

	
class SearchView(APIView):
	def get(self, request, text):
		popularProducts = PopularProduct.objects.all()
		products = Product.objects.all()

		foundPopularProducts = []
		foundProducts = []

		for popularProduct in popularProducts:
			if text.lower() in popularProduct.name.lower():
				foundPopularProducts.append(popularProduct)
		for product in products:
			if text.lower() in product.name.lower():
				foundProducts.append(product)

		popularProductSerializer = PopularProductsSerializer(foundPopularProducts, many = True)
		productSerializer = ProductsSerializer(foundProducts, many=True)

		return Response({"Products":(popularProductSerializer.data + productSerializer.data)})



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
	def get(self, request, newsSlug=''):
		if newsSlug =='':
			news = New.objects.all()
			serializer = NewSerializer(news, many=True)
			return Response({"News": serializer.data})
		else:
			news = News.objects.get(slug=newsSlug)
			serializer = NewSerializer(news, many=False)
			return Response({"News": serializer.data})


class LoginView(APIView):
	def post(self, request):
		user=json.loads(request.body)
		
		email = user.get('email')
		password = user.get('password')

		user = authenticate(username=email, password=password)
		if user is not None:
			token = Token.objects.create(user=user)
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=201)



class CheckEmail(APIView):
	def post(self, request):
		user=json.loads(request.body)
		random_number = random.randint(1000,9999)
		msg = MIMEMultipart()
		message = str(random_number)
		password = "Xxok0LKq"
		msg['From'] = "xiaomitronshop@gmail.com"
		msg['To'] = user.get('email')
		msg['Subject'] = "XiaomiTron - код подтверждения email"
		msg.attach(MIMEText(message, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com: 587')
		server.starttls()
		server.login(msg['From'], password)
		server.sendmail(msg['From'], msg['To'], msg.as_string())
		server.quit()

		return HttpResponse(random_number)

class ResiterView(APIView):
	def post(self, request):
		user = json.loads(request.body)
		
		name = user.get('name')
		surname = user.get('surname')

		email = user.get('email')
		phone = user.get('phone')
		password = user.get('password')
		
		try:
			userLog = User.objects.get(username=email)
		except User.DoesNotExist:
			userLog = True
		else:
			userLog = False
		
		if userLog:
			user = User.objects.create_user(username=name + ' ' + surname,
											password=password,
											first_name = name,
											last_name = surname,
											email = email)
			profile = Profile(user=user, phone = phone)
			profile.save()
			user.save()
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
	
