from django.db import models
from django.contrib.auth.models import User

class CartAll(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Cart(CartAll):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_ordered = models.BooleanField(default=False)

    def total_price(self):
        total = 0
        for i in self.items.all():
            total += i.quantity * i.product.price
        return total
    
    def __str__(self):
        return f'{self.user}\'s cart {self.is_ordered}'
    
class CartItem(CartAll):
    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE, null=True, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)

    def total_price_product(self):
        return self.quantity * self.product.new_price

    def __str__(self):
        return f'{self.product.name}({self.cart.user})'

class Order(CartAll):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_email = models.EmailField(max_length=254)
    status = models.CharField(max_length=255, default='Ordered')
    cart = models.OneToOneField("carts.Cart", on_delete=models.CASCADE, related_name='order')
    
    def __str__(self):
        return (f'{self.cart.user} order')