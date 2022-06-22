from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


# Create your views here.
def store(request, category_slug=None):
    products = Product.objects.all().filter(is_available=True)
    return render(request, 'store/store.html', {"products": products})


def product_detail(request, product_slug):
    return render(request, 'store/product-detail.html')

