import unittest

from pyscience.algebra import Variable, Monomial, Polynomial


class TestAlgebra(unittest.TestCase):

    def test_evaluate(self):
        self.assertEqual(Variable('x').evaluate(x=2),
                         2)

        self.assertEqual(Monomial(variables='xx', coefficient=2).evaluate(x=1),
                         2)

        self.assertEqual(str(Monomial(variables='xy', coefficient=5).evaluate(x=2)),
                         '10y')

        p = Polynomial(monomials=[Monomial(variables='xx', coefficient=3),
                                  Monomial(variables='xyy', coefficient=1)],
                       numerical_term=4)

        self.assertEqual(p.evaluate(x=2, y=5), 66)


if __name__ == '__main__':
    unittest.main()
