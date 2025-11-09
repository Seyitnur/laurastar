from django.db.models import Q
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import *
from products.serializers import *
from carts.models import *
from carts.serializers import *

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['GET'])
def index(request):
    return Response({"message": "Hi"})

@api_view(['GET'])
def shop(request):
    category = request.GET.get('category')
    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, i):
    product = Product.objects.get(id=i)
    related_products = product.related_products()
    serializer = ProductSerializer(product, many=False)
    serializer2 = ProductSerializer(related_products, many=True)
    return Response({"product": serializer.data, "related_product": serializer2.data})

class ProductSearchView(APIView):
    def get(self, request):
        search = request.GET.get('search')
        products = Product.objects.filter(Q(name_ru__contains=search) | Q(name_tk__contains=search))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'order': serializer.data})