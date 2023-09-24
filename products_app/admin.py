from django.contrib import admin

from .models import Product, ProductsCategory

admin.site.register(Product)
admin.site.register(ProductsCategory)