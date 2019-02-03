from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.http import Http404
# Create your views here.

# Class base view
class ProductFeaturedListView(ListView):
    model = Product
    template_name = 'products/featured_product_list.html'
    queryset = Product.objects.featured()

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    template_name = 'products/featured_product_detail.html'
    queryset = Product.objects.featured()
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    model = Product

    context_object_name = 'products'
    # queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context

# Function base view

def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(request, 'products/product_list_view.html', context)

class ProductDetailSlugView(DetailView):
    model = Product
    # queryset = Product.objects.all()
    context_object_name = 'instance'
    template_name = 'products/product_detail_slug.html'

    # For Custom Model Manager
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug)
            print(instance)

        except Product.DoesNotExist:
            raise Http404("No Product found!")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.get(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Hmm sai")
        return instance


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    # queryset = get_object_or_404(Product, pk=pk)
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    # For Custom Model Manager
    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("No Product ok?")
    #     return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)




    template_name = 'products/product_detail.html'

def product_detail_view(request, pk=None, *args, **kwargs):
    # queryset = get_object_or_404(Product, pk=pk)
    # try:
    #     queryset = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     print("product does not exist")
    #     raise Http404("Product does not exist")
    # except:
    #     raise Http404("Hmmm sai sai")

    # qs = Product.objects.filter(id = pk)
    # For Custom Model Manager
    qs = Product.objects.get_by_id(pk)
    print(qs)
    if qs is None:
        raise Http404("No Product ok?")


    context = {'object': qs}
    return render(request, 'products/product_detail.html', context)
