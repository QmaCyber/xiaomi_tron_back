from rest_framework import serializers

class ProductsSerializer(serializers.Serializer):
	category = serializers.CharField()
	name = serializers.CharField()
	image = serializers.ImageField()
	description = serializers.CharField()
	price = serializers.IntegerField()
	stock = serializers.IntegerField()
	slug = serializers.CharField()
	available = serializers.BooleanField()
	created = serializers.DateTimeField()
	updated = serializers.DateTimeField()

class PopularProductsSerializer(serializers.Serializer):
	name = serializers.CharField()
	image = serializers.ImageField()
	description = serializers.CharField()
	oldprice = serializers.IntegerField()
	price = serializers.IntegerField()
	stock = serializers.IntegerField()
	slug = serializers.CharField()
	available = serializers.BooleanField()
	created = serializers.DateTimeField()
	updated = serializers.DateTimeField()

class imagesSliderSerializer(serializers.Serializer):
	name = serializers.CharField()
	image = serializers.ImageField()