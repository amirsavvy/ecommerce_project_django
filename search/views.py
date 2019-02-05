from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.

class SearchProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
