from django.contrib import admin
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'product_kod', 'name']
    search_fields = ['product_kod', 'category']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
