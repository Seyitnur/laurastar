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
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_email = models.EmailField(max_length=254)
    status = models.CharField(max_length=255, default='Ordered')
    
    def __str__(self):
        return (f'{self.customer_name} order')
