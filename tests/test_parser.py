import unittest

from pyscience.parser import split_expression, expand


class TestParser(unittest.TestCase):

    def test_split_expression(self):
        self.assertEqual(split_expression('2x+34'),
                         ['2', 'x', '+', '34'])

    def test_expand(self):
        self.assertEqual(expand('2x+4'),
                         '2*x+4')
        self.assertEqual(expand('x(2x-2)'),
                         'x*(2*x-2)')
        self.assertEqual(expand('67'),
                         '67')
        self.assertEqual(expand('x6'),
                         'x*6')


if __name__ == '__main__':
    unittest.main()
