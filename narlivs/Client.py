import urllib.parse
from robobrowser import RoboBrowser


BASE_URL = 'http://www.narlivs.se'


def build_path(path):
    return urllib.parse.urljoin(BASE_URL, path)


class InvalidCredentials(Exception):
    pass


class Client(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = RoboBrowser(history=True, parser='lxml')

    def _open(self, path):
        url = build_path(path)
        self.browser.open(url)
        return self.browser.parsed

    def get_data(self, path, retry=True):
        """Loads the given path making sure that the request is authenticated"""
        response = str(self._open(path))
        if 'Logga ut' not in response:
            if retry:
                self.authenticate(self.username, self.password)
                return self.get_data(path, retry=False)
            raise InvalidCredentials()
        return response

    def authenticate(self, username, password):
        self._open('/')
        login_form = self.browser.get_form()
        login_form['LoginForm_Login'].value = username
        login_form['LoginForm_Password'].value = password
        self.browser.submit_form(login_form)


if __name__ == '__main__':
    import os
    c = Client(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    assert c.get_data('/')
