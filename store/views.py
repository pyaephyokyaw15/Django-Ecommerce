from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from django.views.generic import ListView, DetailView
from django.db.models import Q


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


class ProductSearchView(ListView):
    model = Product
    template_name = 'store/store.html'
    paginate_by = 2
    context_object_name = 'products'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword))
        else:
            products = Product.objects.filter(is_available=True)
        return products


