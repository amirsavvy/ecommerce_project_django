from django.conf.urls import url
from products.views import ProductListView, product_detail_view, product_list_view, ProductDetailView


app_name = 'products'

urlpatterns = [
    url(r'lists-cbv/', ProductListView.as_view(), name='product_list'),
    url(r'lists-fbv/', product_list_view, name='product_list1'),
    url(r'detail/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'detail-fbv/(?P<pk>\d+)/$', product_detail_view),


]
