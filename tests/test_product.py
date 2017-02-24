from .base import NarlivsTestCase


class ProductTests(NarlivsTestCase):
    def testRetrieval(self):
        data = self.narlivs.get_product(ean='7310350109265').data
        self.assertEqual(data['ean'], '7310350109265')
        self.assertEqual(data['sku'], '100102201')
        self.assertIsNotNone(data['price'])
        self.assertIsNotNone(data['image'])

        # Make sure that getting the product by SKU
        # produces the same result
        data = self.narlivs.get_product(sku='100102201').data
        self.assertEqual(data['sku'], '100102201')
