from .base import NarlivsTestCase


class ProductTests(NarlivsTestCase):
    def test_get_product(self):
        data1 = self.narlivs.get_product(ean='7310350109265').data
        self.assertEqual(data1['ean'], '7310350109265')
        self.assertEqual(data1['sku'], '100102201')
        self.assertIsNotNone(data1['price'])
        self.assertIsNotNone(data1['image'])
        self.assertIsNotNone(data1['cart_add_url'])
        self.assertIsNotNone(data1['units'])

        # Make sure that getting the product by SKU
        # produces the same result
        data2 = self.narlivs.get_product(sku='100102201').data
        self.assertEqual(data1, data2)
