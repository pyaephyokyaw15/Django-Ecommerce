from django.urls import path
from . import views

app_name = 'store'


urlpatterns = [
    path('', views.ProductListView.as_view(), name='store'),
    path('categories/<slug:slug>/', views.ProductListView.as_view(), name='products_by_category'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('search/', views.ProductSearchView.as_view(), name='search'),
]
