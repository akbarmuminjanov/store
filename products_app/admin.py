from django.contrib import admin

from .models import Product, Category
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'product_kod', 'name']
    search_fields = ['product_kod', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
