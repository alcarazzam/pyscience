"""
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

from dataclasses import dataclass
from typing import Union


@dataclass
class Square:
    l: Union[int, float]

    @property
    def area(self):
        return self.l ** 2

    @property
    def perimeter(self):
        return self.l * 4


@dataclass
class Triangle:
    b: Union[int, float]
    h: Union[int, float]

    @property
    def area(self):
        return (self.b * self.h) / 2


@dataclass
class Rectangle:
    b: Union[int, float]
    h: Union[int, float]

    @property
    def area(self):
        return self.b * self.h

    @property
    def perimeter(self):
        return 2 * (self.b + self.h)


@dataclass
class Parallelogram:
    b: Union[int, float]
    h: Union[int, float]
    a: Union[int, float]

    @property
    def area(self):
        return self.b * self.h

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)


@dataclass
class Diamond:
    a: Union[int, float]
    d: Union[int, float]
    D: Union[int, float]

    @property
    def perimeter(self):
        return self.a * 4

    @property
    def area(self):
        return (self.d * self.D) / 2


@dataclass
class Polygon:
    L: Union[int, float]
    a: Union[int, float]
    nL: int

    @property
    def perimeter(self):
        return self.L * self.nL

    @property
    def area(self):
        return (self.perimeter * self.a) / 2
