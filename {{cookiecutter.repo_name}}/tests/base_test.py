import unittest

from app import create_app


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['TESTING'] = True
        # to make forms validation work
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        # changes the context to testing
        # if this is not done then the
        # context will
        # be set to original context
        # defined in application.py
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
