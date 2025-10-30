from products.models import *
from carts.models import *

def all_data(request):
    category = Category.objects.all()

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, is_ordered=False)
    else:
        cart = None
    
    context = {
        'category':category,
        'cart':cart,
    }

    return context
