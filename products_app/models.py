from django.db import models

class ProductsCategory(models.Model):

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "ProductsCategories"

    name = models.CharField(max_length=155)
    descriptions = models.TextField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    descriptions = models.TextField(null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="product_image")

    def __str__(self):
        return self.name