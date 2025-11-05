from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey("products.Category", on_delete=models.CASCADE)

    def related_products(self):
        products = []
        for i in Product.objects.filter(category=self.category):
            if (i not in products) and (i.id != self.id):
                products.append(i)
        return products

    def __str__(self):
        return self.name

class Image(BaseModel):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey("products.Product", related_name='images', on_delete=models.CASCADE)
