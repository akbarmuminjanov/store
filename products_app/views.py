from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
    return render(request, "index.html")

def product_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    contex = {
        "category": category,
        "categoryies": categories,
        "products": products
    }
    return render(request, "products.html", contex)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, "detail.html", {'product':product})

def category_page(request, category_id):
    product = Product.objects.filter(category=category_id)
    context = {       
        "products":product
    }
    return render(request, "products.html", context)

