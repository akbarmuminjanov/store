from django.urls import path

from .views import index, product_view, category_page, profile

urlpatterns = [
   path('', index, name="index_view"),
   path('products/', product_view, name="product_view"),
   path('products/<int:category_id>/', category_page, name="category-list"),
   path('profile/', profile, name="profile"),
]