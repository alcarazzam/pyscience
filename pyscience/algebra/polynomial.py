"""
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
"""
"""
Created by Manuel Alcaraz on 22 May, 2018
"""

from pyscience import algebra
from pyscience.algebra.monomial import count_variables
from pyscience.math.fraction import Fraction

class Polynomial:
    def __init__(self, *args, **kwargs):
        self.monomials = kwargs.get('monomials', [])
        self.numerical_term = kwargs.get('numerical_term', 0)
    
    @property
    def degree(self):
        return max([x.degree for x in self.monomials])
    
    @property
    def list_of_variables(self):
        # TODO: Optimize function.
        ml = [x.list_of_variables for x in self.monomials]
        ml = [''.join(x) for x in ml]
        ml = ''.join(ml)
        ml = count_variables(ml).keys()
        ml = list(ml)
        return ml

    def __add__(self, value):
        if isinstance(value, algebra.Monomial):
            n=0
            len_monomials = len(self.monomials)
            for x in self.monomials:
                try:
                    # Intentar sumar los monomials
                    # "x += value" no vale porque devuelve un polinomio si no son iguales
                    if algebra.monomial.count_variables(x.variables) == algebra.monomial.count_variables(value.variables):
                        if self.monomials[self.monomials.index(x)].coefficient + value.coefficient != 0:
                            self.monomials[self.monomials.index(x)] += value
                        else:
                            del self.monomials[self.monomials.index(x)]
                    else:
                        raise ValueError
                    break
                except ValueError:
                    pass
                n+=1
            if n >= len_monomials: # No ha habido ninguno que sea igual
                self.monomials.append(value)
            if len(self.monomials) == 0:
                return self.numerical_term
            return self
        elif isinstance(value, Polynomial):
            result = algebra.Polynomial()
            
            for monomial in self.monomials:
                result += monomial
            
            for monomial in value.monomials:
                result += monomial
            
            result += self.numerical_term + value.numerical_term
            
            return result
            
        elif isinstance(value, int):
            self.numerical_term += value
            return self
        elif isinstance(value, algebra.Variable):
            return self + algebra.Monomial(variables=value.name)
        else:
            raise TypeError(f'Cannot add a Polynomial to {type(value)}')
    
    def __radd__(self, value):
        return self + value

    def __sub__(self, value):
        if isinstance(value, algebra.Monomial):
            n=0
            len_monomials = len(self.monomials)
            for x in self.monomials:
                try:
                    # Intentar restar los monomials
                    # "x -= value" no vale porque devuelve un polinomio si no son iguales
                    if algebra.monomial.count_variables(x.variables) == algebra.monomial.count_variables(value.variables):
                        if self.monomials[self.monomials.index(x)].coefficient - value.coefficient != 0:
                            self.monomials[self.monomials.index(x)] -= value
                        else:
                            del self.monomials[self.monomials.index(x)]
                    else:
                        raise ValueError
                    break
                except ValueError:
                    pass
                n+=1
            if n >= len_monomials:
                # No ha habido ninguno que concuerde
                self.monomials.append(value)
            
            if len(self.monomials) == 0:
                return self.numerical_term
            return self
        elif isinstance(value, Polynomial):
            result = Polynomial()
            
            for monomial in self.monomials:
                result -= monomial
            
            for monomial in value.monomials:
                result -= monomial
            
            result.numerical_term += self.numerical_term - value.numerical_term
            
            return result
                
        elif type(value) is int:
            self.numerical_term -= value
            return self
        elif type(value) is algebra.Variable:
            return self - algebra.Monomial(variables=value.name, coefficient=-1)
        else:
            raise TypeError(f'Cannot subtract a Polynomial to {type(value)}')

    def __truediv__(self, value):
        if isinstance(value, int):
            # TODO: Simplify division
            return Fraction(self, value)
        elif isinstance(value, Fraction):
            R=[]
            for x in self.monomials:
                R.append(x/value)
            if self.numerical_term != 0:
                if self.numerical_term % value == 0:
                    numerical_term = int(self.numerical_term / value)
                else:
                    numerical_term = Fraction(self.numerical_term, value)
            else:
                numerical_term = 0
            return algebra.Polynomial(monomials=R, numerical_term=numerical_term)
        elif isinstance(value, algebra.Variable):
            raise NotImplementedError
        elif isinstance(value, algebra.Monomial):
            #print('dividing', self, value)
            R=[]
            numerical_term = 0
            for x in self.monomials:
                result = x/value
                if result.variables == "":
                    numerical_term += result.coefficient
                else:
                    R.append(result)
            if self.numerical_term != 0:
                if self.numerical_term % value.coefficient == 0:
                    result = self.numerical_term / value.coefficient
                    if type(result) is float:
                        result = int(result)
                    R.append(algebra.Monomial(coefficient=result, variables=value.variables))
                else:
                    R.append(algebra.Monomial(coefficient=Fraction(self.numerical_term, value.coefficient),variables=value.variables))
            return Polynomial(monomials=R, numerical_term=numerical_term)
        elif isinstance(value, Polynomial):
            raise NotImplementedError
        else:
            return TypeError(f'Cannot divide a Polynomial by {type(value)}')

    def __mul__(self, value):
        if isinstance(value, (algebra.Monomial, int)):
            result = algebra.Polynomial()
            
            for monomial in self.monomials:
                result += monomial * value
            
            if self.numerical_term:
                result += self.numerical_term * value
            
            return result
        elif isinstance(value, Polynomial):
            result = algebra.Polynomial()
            
            for monomial in self.monomials:
                result += monomial * value
                
            result += self.numerical_term * value
            
            return result
        elif isinstance(value, algebra.Variable):
            result = Polynomial()
            
            for monomial in self.monomials:
                result += monomial * value
                
            if self.numerical_term:
                result += self.numerical_term * value
            
            return result
        else:
            raise TypeError(f'Cannot multiply a Polynomial by {type(value)}')
    
    def __rmul__(self, value):
        return self * value

    def __pow__(self, value, mod=None):
        if mod:
            raise NotImplementedError
        
        R = []
        
        for x in self.monomials:
            R.append( x ** value )

        if self.numerical_term != 0:
            R.append(self.numerical_term ** value)
        
        RT = 0
        #print(R)
        for x in R:
            RT += x
        return RT
        

    def __str__(self):
        R=''
        for x in self.monomials:
            R+= '+'+str(x) if x.coefficient > 0 else str(x)
        if self.numerical_term != 0:
            if self.numerical_term <0:
                R+=str(self.numerical_term)
            else:
                R+='+'+str(self.numerical_term)
        return R

    def __neg__(self):
        return Polynomial(monomials=[-x for x in self.monomials], numerical_term=-self.numerical_term)
    
    def __pos__(self):
        return self

    def __repr__(self):
        return f'<Polynomial {self}>'
