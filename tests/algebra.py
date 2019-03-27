import unittest

from pyscience.algebra import Variable, Monomial

class TestAlgebra(unittest.TestCase):
    
    def test_evaluate(self):
        self.assertEqual(Variable('x').evaluate(x=2),
                         2)
        
        self.assertEqual(Monomial(variables='xx', coefficient=2).evaluate(x=1),
                         2)
        
        self.assertEqual(str(Monomial(variables='xy', coefficient=5).evaluate(x=2)),
                         '10x')


if __name__ == '__main__':
    unittest.main()
