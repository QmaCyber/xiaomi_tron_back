from rest_framework import serializers


class ProductsSerializer(serializers.Serializer):
	category = serializers.CharField()
	name = serializers.CharField()
	image = serializers.ImageField()
	description = serializers.CharField()
	price = serializers.CharField()
	stock = serializers.IntegerField()
	slug = serializers.CharField()
	created = serializers.DateTimeField()

class PopularProductsSerializer(serializers.Serializer):
	name = serializers.CharField()
	slug = serializers.CharField()
	image = serializers.ImageField()
	description = serializers.CharField()
	oldprice = serializers.CharField()
	oldprice = serializers.IntegerField()
	price = serializers.CharField()
	stock = serializers.IntegerField()
	created = serializers.DateTimeField()


class CategorySerializer(serializers.Serializer):
	name = serializers.CharField()
	slug = serializers.CharField()


class ImagesSliderSerializer(serializers.Serializer):
	color_text = serializers.CharField()
	name = serializers.CharField()
	image = serializers.ImageField()


class NewSerializer(serializers.Serializer):
	title = serializers.CharField()
	shortDescription = serializers.CharField()
	image = serializers.ImageField()
	url = serializers.CharField()
	created = serializers.DateTimeField()


class ReviewSerializer(serializers.Serializer):
	name = serializers.CharField()
	reviewUrl = serializers.CharField()
	video = serializers.CharField()

class RandomNumverSerializer(serializers.Serializer):
	randomNumber = serializers.IntegerField()