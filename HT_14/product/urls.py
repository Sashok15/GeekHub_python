from django.conf.urls import url

from product.views import *


app_name = 'product'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<id>\d+)/$', subcategory_product,
        name='subcategory-product'),
    url(r'^(?P<id>\d+)/details/$', product_details,
        name='product-details'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^order/$', make_order, name='order'),
    url(r'^(?P<id>\d+)/remove_product/$',
        delete_product_from_session, name='remove')
]