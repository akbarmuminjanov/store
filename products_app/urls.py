from django.urls import path

from .views import index_view, product_view

urlpatterns = [
   path('', index_view, name="index_view"),
   path('products/', product_view, name="product_view"),
]