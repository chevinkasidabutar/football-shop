from django.test import TestCase

# Create your tests here.
# main/tests.py
from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.p = Product.objects.create(
            name="Ball",
            price=100000,
            description="Bola futsal",
            thumbnail="https://example.com/ball.jpg",
            category="Bola",
            is_featured=False,
            stock=2,
        )

    def test_str_and_stock(self):
        self.assertEqual(str(self.p), "Ball")
        self.assertTrue(self.p.is_in_stock)
        self.p.sell(1)
        self.p.refresh_from_db()
        self.assertEqual(self.p.stock, 1)
        self.assertEqual(self.p.sold_count, 1)

class HomeViewTest(TestCase):
    def test_home_returns_200(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
