from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r"^(?P<slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)/$",
        views.product_details,
        name="details",
    ),
    url(
        r"^digital-download/(?P<token>[0-9A-Za-z_\-]+)/$",
        views.digital_product,
        name="digital-product",
    ),
    url(
        r"^category/(?P<slug>[a-z0-9-_]+?)-(?P<category_id>[0-9]+)/$",
        views.category_index,
        name="category",
    ),
    url(
        r"(?P<slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)/add/$",
        views.product_add_to_checkout,
        name="add-to-checkout",
    ),
    url(
        r"^collection/(?P<slug>[a-z0-9-_/]+?)-(?P<pk>[0-9]+)/$",
        views.collection_index,
        name="collection",
    ),  
    url(
        r"^new_items/(\d+)$", views.new_items, name="new_items"
    ),

    url(
        r"^price_under/(\d+)/(\d+)$", views.price_under, name="price_under"
    ),

    url(
        r"^category_items/(\w+)/(\d+)$", views.category_items, name="category_items"
    ),
]
