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
        cart = Cart(request)
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save order
            order = form.save(commit=False)
            order.customer = request.user
            order.total_price = cart.get_total_price()
            order.save()

            order.order_number = datetime.date.today().strftime("%Y%m%d") + str(order.id)
            order.save()

            cart = Cart(request)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], quantity=item['qty'], price=item['price'])
            cart.clear()
            return redirect('store:store')
        else:
            print(form.errors)

    else:
        form = OrderForm()

    return render(request, 'orders/place_order.html', {'form': form})