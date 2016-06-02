import unittest2

class MyTestCase(unittest2.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        
    def test_another(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest2.main()
