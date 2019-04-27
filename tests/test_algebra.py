import unittest

from pyscience.algebra import Variable, Monomial, Polynomial, Equation, get_variables


class TestAlgebra(unittest.TestCase):

    def test_get_variables(self):
        x, y, z = get_variables('x y z')

        self.assertEqual(x, Variable('x'))
        self.assertEqual(y, Variable('y'))
        self.assertEqual(z, Variable('z'))

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

    def test_second_degree_equations(self):
        x = get_variables('x')[0]

        eq1 = Equation(x ** 2 + 2 * x - 8)
        self.assertEqual(eq1.solution, [2.0, -4.0])

        eq2 = Equation(2 * x ** 2 + 6 * x + 4)
        self.assertEqual(eq2.solution, [-1.0, -2.0])

        eq3 = Equation(-4 * x ** 2 + 36)
        self.assertEqual(eq3.solution, [-3.0, 3.0])

        eq4 = Equation(-3 * x ** 2 + 12 * x)
        self.assertEqual(eq4.solution, [0, 4.0])


if __name__ == '__main__':
    unittest.main()
