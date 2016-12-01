import decimal
from .Base import BaseAPI, NarlivsException
from .Client import build_path

SEARCH_URL = ('/is-bin/INTERSHOP.enfinity/WFS/Axfood-NWP2-Site/sv_SE/-'
              '/SEK/ViewParametricSearch-SimpleOfferSearch?searchTerm='
              '{search_term}')


class Product(BaseAPI):
    """Represents a single product."""

    def __init__(self, client, ean=None, sku=None):
        super().__init__(client)
        assert ean is not None or sku is not None
        self.sku = sku
        self.ean = ean
        self.data = self.retrieve(self.ean or self.sku)

    def retrieve(self, search_term):
        """Retrieves product details for given search term."""
        url = SEARCH_URL.format(search_term=search_term)
        self.client.get_data(url)

        def element(s):
            query = '.productListContainer .productInnerContainer {}'.format
            return self.client.browser.select(query(s))[0]

        def text(s):
            return element(s).text.strip()

        def prop(n):
            return text('tr:nth-of-type({}) td:nth-of-type(2)'.format(n))

        def money(x):
            """Convert from Narlivs money format to a decimal."""
            return decimal.Decimal(x.split()[0].replace(',', '.'))

        thumbnail_url = build_path(element('img')['src'])

        data = {
            'name': text('.productName'),
            'sku': prop(2),
            'ean': prop(3),
            'price': money(text('tbody .price')),
            'image': thumbnail_url.replace('thumbnails', 'images')
        }

        # Verify that the retrieved product matches the given EAN or SKU.
        msg = 'Retrieved product does not match given {} ({} != {})'.format

        if self.sku is not None and self.sku != data['sku']:
            raise NarlivsException(msg('SKU', self.sku, data['sku']))

        if self.ean is not None and self.ean != data['ean']:
            raise NarlivsException(msg('EAN', self.ean, data['ean']))

        return data

    def __repr__(self):
        fmt = '<{} sku={o[sku]} name={o[name]} >'.format
        tp = type(self)
        return fmt(tp.__name__, o=self.data)
