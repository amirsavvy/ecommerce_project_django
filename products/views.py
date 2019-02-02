from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.shortcuts import render, get_object_or_404
from products.models import Product
# Create your views here.

# Class base view
class ProductListView(ListView):
    model = Product

    context_object_name = 'products'
    queryset = Product.objects.all()

    template_name = 'products/product_list.html'
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context

# Function base view

def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(request, 'products/product_list_view.html', context)

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    # queryset = get_object_or_404(Product, pk=pk)
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    template_name = 'products/product_detail.html'

def product_detail_view(request, pk=None, *args, **kwargs):
    queryset = get_object_or_404(Product, pk=pk)
    context = {'object': queryset}
    return render(request, 'products/product_detail.html', context)
