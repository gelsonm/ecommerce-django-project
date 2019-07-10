# from django.views import ListView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context


def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk) #id
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "detail.html", context)