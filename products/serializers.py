from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['image', 'order']

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name_ru', 'name_tk', 'price', 'category', 'description_ru', 'description_tk', 'main_image', 'images']
    
    def get_images(self, obj):
        request = self.context.get("request")
        images = obj.images.exclude(order=1).order_by('order')
        return {img.order: request.build_absolute_uri(img.image.url) for img in images}
    
    def get_main_image(self, obj):
        request = self.context.get("request")
        img = obj.images.filter(order=1).first()
        return request.build_absolute_uri(img.image.url) if img else None
