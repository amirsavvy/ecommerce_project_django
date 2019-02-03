from django.conf.urls import url
from products.views import (
        ProductListView,
        product_detail_view,
        product_list_view,
        ProductDetailView,
        ProductDetailSlugView,
        ProductFeaturedListView,
        ProductFeaturedDetailView
        )

app_name = 'products'

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product_list'),
    # url(r'lists-fbv/', product_list_view, ),
    # url(r'featured/', ProductFeaturedListView.as_view(), name='product_featured'),
    # url(r'featured-detail/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    # url(r'detail-cbv/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # url(r'detail-fbv/(?P<pk>\d+)/$', product_detail_view)




]
