from products_app.models import Category

def category(request):
    categories = Category.objects.all()
    return {"categories":categories}