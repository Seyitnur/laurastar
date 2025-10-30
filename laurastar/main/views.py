from django.shortcuts import render
from products.models import *

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def technologies(request):
    return render(request, 'technologies.html')

def shop(request):
    return render(request, 'shop.html')

def product_detail(request):
    return render(request, 'product_detail.html')

def service(request):
    return render(request, 'service.html')

def search_product(request):
    search = request.POST.get('search')
    products = Product.objects.filter(name__contains=search)

    context = {
        'product':products,
        'search':search,
    }

    return render(request, 'shop.html', context)