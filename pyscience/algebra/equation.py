'''
pyscience - python science programming
Copyright (c) 2019 Manuel Alcaraz Zambrano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import copy
from pyscience import algebra
from pyscience.math import Fraction

def get_degree(value):
    if isinstance(value, (algebra.Monomial, algebra.Polynomial)):
        return value.degree
    elif isinstance(value, int):
        return 1
    return 1

class Equation:
    
    def __init__(self, first_term, second_term=0):
        self.first_term = first_term
        self.second_term = second_term
    
    def solve(self):
        # TODO
        first_term = copy.deepcopy(self.first_term)
        second_term = copy.deepcopy(self.second_term)
        #print('paso 1', first_term, second_term)
        
        if second_term != 0:
            first_term = first_term - second_term
            second_term = 0
            
        #print('paso 2', first_term)
        
        if get_degree(first_term) == 1:
            # First-degree equation
            if isinstance(first_term, algebra.Monomial):
                return 0#- (-algebra.Monomial(self.first_term.variables) / self.first_term.coefficient)
            elif isinstance(first_term, algebra.Polynomial):
                #print('poli')
                # Check if the number of variables is 1
                if len(first_term.list_of_variables) != 1:
                    raise NotImplementedError('Cannot solve a equation with more than one variable')
                
                if first_term.numerical_term % first_term.monomials[0].coefficient == 0:
                    return -(first_term.numerical_term // first_term.monomials[0].coefficient)
                return -Fraction(first_term.numerical_term, first_term.monomials[0].coefficient)
            elif isinstance(first_term, Fraction):
                #print('fraction')
                #ft = first_term - second_term
                #ft = -ft.denominator
                #print('zlsjgsldgfd')
                #print(ft)
                #return Equation(ft.numerator).solve()
                if isinstance(self.second_term, Fraction):
                    a, b = self.first_term.common_denominator(self.second_term)
                    #print(a,b)
                    return Equation(a.numerator, b.numerator).solve()
                elif isinstance(self.second_term, int):
                    a, b = self.first_term.common_denominator(Fraction(self.second_term,1))
                    #print('a, b =',a,b)
                    return Equation(a.numerator, b.numerator).solve()
        
        raise NotImplementedError('Cannot solve a equation with a degree greater than 1')
    
    def __str__(self):
        return f'Eq({self.first_term} = {self.second_term})\nSolution: {self.solve()}'
    
    def __repr__(self):
        return f'<Equation {self.first_term} = {self.second_term}>'
