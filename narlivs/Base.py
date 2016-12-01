class NarlivsException(Exception):
    pass


class BaseAPI(object):
    def __init__(self, client):
        self.client = client
