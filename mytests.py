import unittest

from google.appengine.api import mail
from google.appengine.ext import testbed

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
