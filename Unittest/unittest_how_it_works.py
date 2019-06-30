import unittest


class TestStringMethods(unittest.TestCase):

    def test_0(self):
        print("0. beginning")

    def test_1(self):
        print("1. beginning 2")

    def test_2(self):
        print ("2. test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_7(self):
        print("7. test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_4(self):
        print("4. test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_5_end(self):
        print("5. end")

    def test_6_end_2(self):
        print("6. end 2")

    def test_8_how_tests_run(self):
        print("10. Test are running alphabetically.")


if __name__ == '__main__':
        unittest.main()
