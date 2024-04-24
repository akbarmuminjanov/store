from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator

def index(request):
    return render(request, "index.html")

def product_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    nums = "s"*page_obj.paginator.num_pages

    contex = {
        "category": category,
        "categoryies": categories,
        "page_obj": page_obj,
        "nums":nums
    }
    return render(request, "products.html", contex)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "detail.html", {'product':product, 'cart_product_form':cart_product_form})

# def category_page(request, category_id):
#     product = Product.objects.filter(category=category_id)
#     context = {       
#         "products":product
#     }
#     return render(request, "products.html", context)

