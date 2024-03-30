from .models import Product, Category
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
# from slugify import slugify
