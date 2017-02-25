from .base import NarlivsTestCase


class CartTests(NarlivsTestCase):
    def setUp(self):
        super().setUp()
        self.cart = self.narlivs.get_cart()
        self.cart.clear()

    def test_clear(self):
        self.cart.add_product('101178095')
        self.cart.clear()
        self.assertEqual(self.cart.size(), 0)

    def test_add_product(self):
        self.cart.add_product('101178095')
        self.assertEqual(self.cart.size(), 1)

    def test_size(self):
        self.assertEqual(self.cart.size(), 0)
        self.cart.add_product('101178095')
        self.assertEqual(self.cart.size(), 1)
