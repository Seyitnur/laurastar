from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name_ru', 'name_tk', 'price', 'category', 'description_ru', 'description_tk', 'images']
