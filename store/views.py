from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def store(request, category_slug=None):
    return HttpResponse("Hello World")


def product_detail(request, product_slug):
    return HttpResponse("Hello World")

