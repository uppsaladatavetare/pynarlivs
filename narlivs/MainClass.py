from .Client import Client
from .Product import Product


class Narlivs(object):
    def __init__(self, username, password):
        self.client = Client(username, password)

    def get_product(self, **kwargs):
        return Product(self.client, **kwargs)


if __name__ == '__main__':
    import os
    n = Narlivs(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    print(n.get_product(ean='7310350109265').data)
    print(n.get_product(sku='100102201').data)
