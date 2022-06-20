from django.db import models
from django.urls import reverse
from categories.models import Category


# Create your models here.
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
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name
