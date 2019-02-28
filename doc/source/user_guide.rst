User guide
==========
Pyscience’s interpreter is very easy to use. Start it with::

    pyscience

Working as a calculator
-----------------------
Pyscience uses python ``eval`` function to evaluate expressions after expand it.
You can use pyscience as a normal calculator::

    > 2 + 2
    4
    > 3 * (2 + 3)
    15
    > 3(3+4) # pyscience will transform the expression to 3 * (3 + 4)
    21

Addition
^^^^^^^^
To add two numbers, use the ``+`` operator::

    > 2 + 3
    5

Subtraction
^^^^^^^^^^^
To subtract two number, use the ``-`` operator::

    > 2 – 3
    -1

Multiplication
^^^^^^^^^^^^^^
To multiply two numbers, use the ``*`` operator::

    > 2 * 3
    6

Division
^^^^^^^^
To divide one number by other, use the ``/`` operator::

    > 8 / 2
    4

Powers
^^^^^^
You can create powers using the ``**`` operator like in python::

    > 2 ** 4
    16

or using ^ numbers::

    > 2⁴
    16

Fractions
^^^^^^^^^
The ``F`` (``Fraction``) class provides a way to create and operate with fractions.
Numerator and denominator are divided using a coma. For example::

    > F(2,3) + F(3,4)
    F(17,12)

You can use the same operators for fractions.


Working with algebra
--------------------
Pyscience can operate with Monomials, Variables and Polynomials. Some examples of
what can you do::

    > 2x + 3x
    5x
    > 3x * 6y
    18xy
    > 2x / (2x)
    1

.. note::
    In the last example, you can think why I have put parenthesis for the second Monomial. If you don’t do it, you will divide *2x* by *2* and, AFTER, you will multiply the result by *x*. In this case, the final result is *x²*

Equations
^^^^^^^^^
You can solve first-degree equations with pyscience. It provides the ``Eq`` class
to work with Equations. Terms are separated as normal arguments, with a comma.
Examples::

    > Eq(2x, 10)
    Eq(2x = 10)
    Solution: 5
    > Eq(F(1,2)+x, 1)
    Eq(F(+2x+1/2) = 1)
    Solution: F(1/2)


Working with chemical elements
------------------------------
Pyscience can show you basic information about chemical elements. You can do it
with the ``CE`` function::

    > CE(‘H’)
    ...

If you want to set a specific mass for the element, indicate that between brackets::

    > CE(‘Si(32)’) # Set mass to 32
    ...

Also, you can work with elements which have charge::

    > CE(‘Si2+’)
    ...

If you know the atomic number of a element but not the symbol, you can get the
element by its atomic number::

    > CE(20) # Calcium (Ca)
