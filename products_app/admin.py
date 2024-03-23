from django.contrib import admin

from .models import Product, Category
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'product_id', 'name']
    search_fields = ['product_id', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
