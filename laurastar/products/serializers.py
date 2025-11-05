from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name_ru', 'name_tk']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name_ru', 'name_tk', 'price', 'category', 'description_ru', 'description_tk', 'images']
