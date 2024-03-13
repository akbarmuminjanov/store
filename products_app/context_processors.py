from products_app.models import ProductsCategory

def category(request):
    categories = ProductsCategory.objects.all()
    return {"categories":categories}