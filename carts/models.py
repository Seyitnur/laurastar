from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
class OrderItem(BaseModel):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)
    order = models.ForeignKey("carts.Order", related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name}'

class Order(BaseModel):
    status_choises = [
        ('В ожидании', 'В ожидании'),
        ('В обработке', 'В обработке'),
        ('Доставлен', 'Доставлен'),
    ]

    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_email = models.EmailField(max_length=254)
    customer_address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choises, default='В ожидании')

    def total_price(self):
        total = 0
        for i in self.items.all():
            total += i.quantity * i.product.new_price
        return total
    
    def __str__(self):
        return (f'{self.customer_name} order')
