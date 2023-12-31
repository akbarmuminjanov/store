from django.shortcuts import render
from .models import ProductsCategory, Product

def index_view(request):
    contex = {
        "title": "Store"
    }
    return render(request, "index.html", contex)

def product_view(request):
    category = ProductsCategory.objects.all()
    product = Product.objects.all()
    contex = {
        "title": "Store - Katalog",
        "categoryies": category,
        "products": product
    }
    return render(request, "products.html", contex)
