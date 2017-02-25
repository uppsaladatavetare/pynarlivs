import urllib.parse
from robobrowser import RoboBrowser

BASE_URL = ('http://www.narlivs.se/is-bin/INTERSHOP.enfinity/WFS/'
            'Axfood-NWP2-Site/sv_SE/-/SEK/')


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
        if not path.startswith('http'):
            path = build_path(path)
        self.browser.open(path)
        return self.browser.parsed

    def visit(self, path, retry=True, no_auth_check=False):
        """Loads the given path making sure the request is authenticated.

        If `no_auth_check`, then no authentication check will be performed.
        """
        response = str(self._open(path))
        if not no_auth_check and 'Logga ut' not in response:
            if retry:
                self.authenticate(self.username, self.password)
                return self.visit(path, retry=False)
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
    assert c.visit('/')
