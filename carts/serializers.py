from rest_framework import serializers
from .models import *

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.Serializer):
    customer_name = serializers.CharField(max_length=255)
    customer_phone = serializers.CharField(max_length=255)
    customer_email = serializers.CharField(max_length=255)
    items = OrderItemSerializer(many=True)

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        print(validated_data)
        print(validated_data.pop('items', []))
        order = Order.objects.create(**validated_data)
        for i in items_data:
            OrderItem.objects.create(order=order, **i)
        return order
