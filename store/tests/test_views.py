from unittest import skip
from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse


from store.models import Product, Category
from store.views import ProductDetailView




@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.category1 = Category.objects.create(
            name="Books",
            slug="books",
            description="Book Category",
            # image = models.ImageField(blank=True),
        )

        self.category2 = Category.objects.create(
            name="CDs",
            slug="cds",
            description="CD Category",
            # image = models.ImageField(blank=True),
        )

        self.product1 = Product.objects.create(
            name="Book Product",
            slug="book_product",
            description="This is Testing Product.",
            price=1000,
            image="test_image",
            stock=100,
        )
        self.product1.categories.add(self.category1)

        self.product2 = Product.objects.create(
            name="CD Product",
            slug="cd_product",
            description="This is Testing Product.",
            price=1000,
            image="test_image",
            stock=100,
        )
        self.product2.categories.add(self.category2)

    def test_allowed_host(self):
        """
        Test allowed host.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_store_page(self):
        """
        Test store response status
        """

        # Send get request to index page and store response
        response = self.client.get('/store/')

        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)

        # Make sure all products are returned in the context
        self.assertEqual(response.context["products"].count(), 2)

    def test_products_by_category(self):
        """
        Test products_by_category filter
        """

        # Send get request to index page and store response
        response = self.client.get(reverse('store:products_by_category', args=['books']))
        # response = self.client.get('/store/categories/books/')

        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)

        # Make sure just selected category products are returned in the context
        self.assertEqual(response.context["products"].count(), 1)


    def test_product_detail_page(self):
        """
        Test product_detail page response status
        """

        # Send get request to index page and store response
        response = self.client.get(reverse('store:product_detail', args=['book_product']))
        # response = self.client.get('/store/products/book_product/')

        # Make sure status code is 200
        self.assertEqual(response.status_code, 200)

        # Make sure Product is correct.
        html = response.content.decode('utf8')
        self.assertIn('Book Product', html)



    def test_no_product_found(self):
        """
        Test no matching product
        """
        response = self.client.get('/store/products/dummy/')
        self.assertEqual(response.status_code, 404)