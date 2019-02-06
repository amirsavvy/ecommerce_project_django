from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.

class SearchProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        # Python dic
        method_dic = request.GET
        query = method_dic.get('q', None) # method_dic['q']
        print(query)

        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.featured()
        '''
        icontains = field is contains this
        iexact = field is exactly this

        '''
