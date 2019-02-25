from pyscience.algebra import Monomial as M, Polynomial as P

print(M('xxy', 3).list_of_variables)
print(P([M('xy'), M('x')]).degree)
