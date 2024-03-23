from django.db import models
from .utils import create_new_id

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_id = models.CharField(max_length= 10, editable=False, unique=True, default=create_new_id)
    name = models.CharField(max_length=255)
    descriptions = models.TextField(null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="product_image")

    def __str__(self):
        return self.name