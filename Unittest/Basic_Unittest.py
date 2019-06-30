import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_is_prime(self):
        self.assert_(1 == 1)


if __name__ == '__main__':
    unittest.main()
