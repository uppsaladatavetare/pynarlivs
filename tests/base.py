import os
from vcr_unittest import VCRTestCase
from narlivs import Narlivs


class NarlivsTestCase(VCRTestCase):
    def setUp(self):
        super().setUp()
        username = os.getenv('NARLIVS_USERNAME')
        password = os.getenv('NARLIVS_PASSWORD')
        self.narlivs = Narlivs(username, password)

    def _get_vcr_kwargs(self, **kwargs):
        new_kwargs = super()._get_vcr_kwargs(**kwargs)
        new_kwargs['filter_post_data_parameters'] = [
            'LoginForm_Login',
            'LoginForm_Password'
        ]
        new_kwargs['filter_headers'] = ['Cookie']
        return new_kwargs
