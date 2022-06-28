from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from orders.models import Order, OrderItem
from django.core.mail import send_mail
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
           form.save()

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

@login_required
def dashboard(request):
    orders = Order.objects.order_by('-created_at').filter(customer=request.user)
    orders_count = orders.count()


    context = {
        'orders_count': orders_count,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def my_orders(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    context = {
        'orders': orders,
    }

    send_mail(
        'Ecommerce Email - ',  # subject
        "Hello",  # message
        'pyaephyokyawtest@gmail.com',  # from email
        # [conf_settings.CONTACT_US_FORM_EMAIL_TO],  # to email
        ['pyaekyaw1571999@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'accounts/my_orders.html', context)

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)



    context = {
        'order_items': order_items,
        'order': order,
        'subtotal': 0,
    }
    return render(request, 'accounts/order_detail.html', context)
