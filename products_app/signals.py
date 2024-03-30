from .models import Product, Category
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from slugify import slugify

# @receiver(pre_save, sender=Product)
# def update_product_slug(instance, *args, **kwargs):
#     instance.slug = slugify(instance.name)

# @receiver(pre_save, sender=Category)
# def update_category_slug(instance, *args, **kwargs):
#     instance.slug = slugify(instance.name)