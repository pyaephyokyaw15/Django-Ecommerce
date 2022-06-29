from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(blank=True)

    class Meta:
        # verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('store:products_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="products/")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.name


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review