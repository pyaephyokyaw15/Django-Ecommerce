from django.test import TestCase
from store.models import Product, Category


class TestProduct(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name="Books",
            slug="books",
            description="Testing for Category",
            # image = models.ImageField(blank=True),
        )

        self.data1 = Product.objects.create(
            name="Test Product",
            slug="test_product",
            description="This is Testing Product.",
            price=1000,
            # image = models.ImageField(upload_to="products/"),
            stock=100,
        )

        self.data1.categories.add(category)

    def test_product_model_entry(self):
        data = self.data1
        # print(data)
        # print(data.name, data.slug, data.image,)
        self.assertTrue(isinstance(data, Product))

    def test_category_model_return_name(self):
        data = self.data1
        self.assertEqual(str(data), "Test Product")

    def test_get_url_fun(self):
        data = self.data1
        self.assertEqual(data.get_url(), '/store/products/test_product/')


class TestCategory(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(
            name="Books",
            slug="books",
            description="Testing for Category",
            # image = models.ImageField(blank=True),
        )

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return_name(self):
        data = self.data1
        self.assertEqual(str(data), "Books")

    def test_get_url_fun(self):
        data = self.data1
        self.assertEqual(data.get_url(), '/store/categories/books/')
