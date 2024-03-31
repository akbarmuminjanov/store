# from django.conf.urls import url
from django.urls import path, re_path

from .views import index, product_view, category_page, product_detail

urlpatterns = [
   path('', index, name="index_view"),
   path('products/<int:category_id>/', category_page, name="category-list"),
   path(r'^$', product_view, name='product_view'),
   path(r'^(?P<category_slug>[-\w]+)/$', product_view, name='product_list_by_category'),
   path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
]