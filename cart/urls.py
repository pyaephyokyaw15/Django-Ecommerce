from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
]
