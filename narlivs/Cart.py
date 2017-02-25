from .Base import BaseAPI
from .Product import Product

EMPTY_CART_URL = ('/is-bin/INTERSHOP.enfinity/WFS/Axfood-NWP2-Site/'
                  'sv_SE/-/SEK/ViewRequisition-EmptyBasket')


class Cart(BaseAPI):
    """Represents the shopping cart."""

    def clear(self):
        self.client.visit(EMPTY_CART_URL)

    def add_product(self, sku):
        """Adds a product with given SKU to the cart."""
        product = Product(self.client, sku=sku).data
        # Calling an AJAX-endpoint so the automatic auth check will fail.
        self.client.visit(product['cart_add_url'], no_auth_check=True)

    def size(self):
        """Returns the count of the products in the cart."""
        self.client.visit('/')
        elements = self.client.browser.select('#mini-basket span')
        if not elements:
            return 0
        return int(elements[0].text.strip().split('\xa0')[0])
