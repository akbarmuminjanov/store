from django.urls import path, re_path
from .views import cart_add, cart_remove


urlpatterns = [
    # path(r'^$',name='cart_detail'),
    path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]