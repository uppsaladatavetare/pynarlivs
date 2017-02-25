"""Scrubs cassettes from sensitive data.

vcrpy's `filter_headers` seem to only filter request headers, so we need
to do the response headers filtering ourselves.
"""
import sys
import yaml

data = yaml.load(sys.stdin)

for interaction in data['interactions']:
    interaction['response']['headers'].pop('Set-Cookie', None)

yaml.dump(data, sys.stdout)
