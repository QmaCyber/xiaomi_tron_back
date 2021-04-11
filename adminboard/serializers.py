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
	slug = serializers.CharField()
	image = serializers.ImageField()
	description = serializers.CharField()
	oldprice = serializers.IntegerField()
	newprice = serializers.IntegerField()
	stock = serializers.IntegerField()
	available = serializers.BooleanField()
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
	video = serializers.CharField()
