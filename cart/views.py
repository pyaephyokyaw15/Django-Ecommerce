from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore

from .cart import Cart


# Create your views here.
def cart_view(request):
    return render(request, 'cart/cart.html')

def add_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('cart:cart_view')


def remove_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart:cart_view')

def remove_cart_item(request, product_id):
    cart = Cart(request)
    cart.delete(product_id)
    return redirect('cart:cart_view')