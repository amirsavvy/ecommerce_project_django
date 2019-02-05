from django.conf.urls import url
from products.views import ProductListView
from search.views import SearchProductView


app_name = 'search'

urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name='search_product_list'),
]
