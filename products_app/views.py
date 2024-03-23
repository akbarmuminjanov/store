from django.shortcuts import render
from .models import Product, Category

def index(request):
    return render(request, "index.html")

def product_view(request):
    category = Category.objects.all()
    product = Product.objects.all()
    contex = {
        "title": "Store - Katalog",
        "categoryies": category,
        "products": product
    }
    return render(request, "products.html", contex)

def category_page(request, category_id):
    product = Product.objects.filter(category=category_id)
    context = {       
        "products":product
    }
    return render(request, "products.html", context)

def profile(request):
    return render(request, "users/profile.html")