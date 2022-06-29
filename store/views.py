from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category, ReviewRating
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderItem, Order


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = ReviewRating.objects.filter(product=context['product'])
        context['reviews'] = reviews
        orderitem= Order.objects.filter(customer=self.request.user, orderitem__product=context['product'])
        context['orderitem'] = orderitem
        try:
            review = ReviewRating.objects.filter(reviewer=self.request.user, product=context['product']).first()
            form = ReviewForm(instance=review)
        except:
            form = ReviewForm()
        context['form'] = form
        return context




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


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            review = ReviewRating.objects.filter(reviewer=request.user, product__id=product_id).first()
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.reviewer = request.user
                review.product_id = product_id

                review.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)
