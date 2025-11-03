from products.models import *

def all_data(request):
    category = Category.objects.all()
    
    context = {
        'category':category,
    }

    return context
