from .models import Category, Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductsSerializer
from rest_framework.response import Response
from .models import Product

class ProductsView(APIView):
	def get(self, request):
		Products = Product.objects.all()
		serializer = ProductsSerializer(Products, many=True)
		return Response({"products": serializer.data})