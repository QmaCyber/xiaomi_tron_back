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


class CategorySerializer(serializers.Serializer):
	name = serializers.CharField()
	slug = serializers.CharField()


class ImagesSliderSerializer(serializers.Serializer):
	colors = serializers.CharField()
	name = serializers.CharField()
	image = serializers.ImageField()


class NewSerializer(serializers.Serializer):
	name = serializers.CharField()
	title = serializers.CharField()
	slug = serializers.CharField()
	image = serializers.ImageField()
	created = serializers.DateTimeField()
	description = serializers.CharField()
	content = serializers.CharField()


class ReviewSerializer(serializers.Serializer):
	name = serializers.CharField()
	reviewUrl = serializers.CharField()