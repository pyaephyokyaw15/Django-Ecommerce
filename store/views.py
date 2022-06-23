from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from django.views.generic import ListView, DetailView


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'store/store.html'
    paginate_by = 2
    context_object_name = 'products'

    def get_queryset(self):
        try:
            category = Category.objects.get(slug=self.kwargs.get('slug'))
            return Product.objects.filter(categories=category, is_available=True)
        except Category.DoesNotExist:
            return Product.objects.filter(is_available=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product-detail.html'
    context_object_name = 'product'
