from rest_framework import serializers


class ProductsSerializer(serializers.Serializer):
	category = serializers.CharField()
	name = serializers.CharField()
	image = serializers.ImageField()
	description = serializers.CharField()
	price = serializers.CharField()
	stock = serializers.IntegerField()
	slug = serializers.CharField()
	available = serializers.BooleanField()
	created = serializers.DateTimeField()
<<<<<<< HEAD
	updated = serializers.DateTimeField()
=======


>>>>>>> 3ca6c58c795d5a056c207ba48db833a61352ba42


class PopularProductsSerializer(serializers.Serializer):
	name = serializers.CharField()
	slug = serializers.CharField()
	image = serializers.ImageField()
	description = serializers.CharField()
<<<<<<< HEAD
	oldprice = serializers.CharField()
	price = serializers.CharField()
=======
	oldprice = serializers.IntegerField()
	newprice = serializers.IntegerField()
>>>>>>> 3ca6c58c795d5a056c207ba48db833a61352ba42
	stock = serializers.IntegerField()
	available = serializers.BooleanField()
	created = serializers.DateTimeField()
<<<<<<< HEAD
	updated = serializers.DateTimeField()
=======
>>>>>>> 3ca6c58c795d5a056c207ba48db833a61352ba42


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
<<<<<<< HEAD
	reviewUrl = serializers.CharField()

=======
	video = serializers.CharField()
>>>>>>> 3ca6c58c795d5a056c207ba48db833a61352ba42
