from django.shortcuts import render
from rest_framework import generics

from products.models import *
from products.serializers import *
from carts.models import *
from carts.serializers import *

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def index(request):

    ironing_systems = Product.objects.filter(category='Гладильные системы')[:2]
    steam_generators = Product.objects.filter(category='Парогенераторы')[:2]
    steamers = Product.objects.filter(category='Отпариватели')[:2]

    context = {
        'ironing_systems': ironing_systems,
        'steam_generators': steam_generators,
        'steamers': steamers,
    }

    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def technologies(request):
    return render(request, 'technologies.html')

def shop(request, i):
    category = Category.objects.get(id=i)
    products = Product.objects.filter(category=category)

    context = {
        'products': products,
    }

    return render(request, 'shop.html', context)

def product_detail(request, i):

    product = Product.objects.get(id=i)
    related_products = product.related_products()

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'product_detail.html', context)

def service(request):
    return render(request, 'service.html')

def cart(request):

    context = {}

    return render(request, 'cart.html', context)

def search_product(request):
    search = request.POST.get('search')
    products = Product.objects.filter(name__contains=search)

    context = {
        'product':products,
        'search':search,
    }

    return render(request, 'shop.html', context)

def checkout_order(request):
    pass
