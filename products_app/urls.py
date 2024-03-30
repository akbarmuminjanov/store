from django.conf.urls import url
from django.urls import path

from .views import index, product_view, category_page, product_detail

urlpatterns = [
   path('', index, name="index_view"),
   path('products/<int:category_id>/', category_page, name="category-list"),
   url(r'^$', product_view, name='product_view'),
   url(r'^(?P<category_slug>[-\w]+)/$', product_view, name='product_list_by_category'),
   url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
]