#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

here = path.dirname(path.abspath(__file__))
long_description = None

try:
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    pass

setup(
    name='pynarlivs',
    description='Client library for the non-existent Narlivs API.',
    long_description=long_description,
    author='Krzysztof Jagiello',
    author_email='me@kjagiello.com',
    url='https://github.com/uppsaladatavetare/pynarlivs',
    version='0.9.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT license',
    zip_safe=False,
    test_suite='tests',
    install_requires=[
        'robobrowser==0.5.3',
        'lxml==3.6.4',
    ],
    tests_require=[
        'vcrpy==1.10.5',
        'vcrpy-unittest==0.1.6',
        'coverage==4.3.4',
    ],
)
