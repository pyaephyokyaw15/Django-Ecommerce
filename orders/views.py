from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart
import datetime
from .forms import OrderForm


# Create your views here.
def place_order(request):


    # cart = Cart(request)
    # order = Order.objects.create(customer=request.user)
    #
    # for item in cart:
    #     OrderItem.objects.create(order=order, product=item['product'], quantity=item['qty'], price=item['price'])
    #
    # return render(request, 'orders/checkout.html')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save order
            order = form.save(commit=False)
            order.customer = request.user
            order.save()

            cart = Cart(request)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['qty'], price=item['price'])
            cart.clear()
            return redirect('store:store')


    else:
        form = OrderForm()

    return render(request, 'orders/place_order.html', {'form': form})