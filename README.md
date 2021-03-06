# pynarlivs

![https://pypi.python.org/pypi/pynarlivs/](https://img.shields.io/pypi/v/pynarlivs.svg)
![https://travis-ci.org/uppsaladatavetare/pynarlivs/](https://api.travis-ci.org/uppsaladatavetare/pynarlivs.svg?branch=master)
![https://codecov.io/gh/uppsaladatavetare/pynarlivs/](https://codecov.io/github/uppsaladatavetare/pynarlivs/coverage.svg?branch=master)

Ever wanted to interact with [Närlivs](http://www.narlivs.se) using an API?
Yep, there is none. We are here to make your life easier! This library aims
to provide a Pythonic interface for some basic functionalities on Narlivs,
i.e. retrieving product information (or, in future, automating the order
process).

## Requirements

- Python 3.4+

## What do we use pynarlivs for?

When receiving a delivery from Narlivs, we get a delivery receipt both on paper
and in PDF format. We parse the PDF file programatically in order to automatically
update the in-stock product quantities.

## Quickstart guide

Install using pip:

```bash
pip install pynarlivs
```

Retrieve product information using its EAN code:
```python
>>> from narlivs import Narlivs
>>> client = Narlivs('username', 'password')
>>> product = client.get_product(ean='7310350109265')
>>> product
<Product sku=100102201 name=BRIO FRUKT  PÅSE >
>>> product.data
{'ean': '7310350109265',
 'image': '(...)/product/products/images/7310350109265.jpg',
 'name': 'BRIO FRUKT  PÅSE',
 'price': Decimal('3.99'),
 'sku': '100102201'}
```

## License

MIT License. Please see the LICENSE file.
