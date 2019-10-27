import unittest
import streetaddress

class TestStreetAddress(unittest.TestCase):
    def setUp(self):
        self.handler = streetaddress.StreetAddress()
    def test_is_zip5(self):
        self.assertTrue(self.handler.is_zip5("90210"))

if __name__ == '__main__':
    unittest.main()