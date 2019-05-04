User guide
==========
Pyscience’s interpreter is very easy to use. Start it with::

    pyscience


Interpreter
-----------
The interpreter has build-in functions for more functionality. They start with
a ``:`` followed by his name.

To exit the interpreter, type ``exit``, ``quit`` or ``q``

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

    > 2 - 3
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
You can solve first and second-degree equations with pyscience. It provides the 
``Eq`` class to work with equations. Terms are separated as normal arguments, 
with a comma.
Examples::

    > Eq(2x, 10)
    Equation(2x = 10)
    > Eq(F(1,2)+x, 1)
    Equation(F(+2x+1/2) = 1)

To solve an equation, use the ``:solve`` function::

    > Eq(2x, 10) :solve
    5

Evaluating expressions
^^^^^^^^^^^^^^^^^^^^^^
You can evaluate any expression with the ``:evaluate`` function::

    > 2x :evaluate x=5
    10
    > 3xy+9 :evaluate x=7                                                                                                                                                       
    +21y+9


Working with chemical elements
------------------------------
Pyscience can show you basic information about chemical elements. You can do it
with the ``Ce`` function::

    > Ce('H') # Get element by its symbol
    ...
    > Ce('Silicon') # Get element by its name
    ...

If you want to set a specific mass for the element, indicate that between
brackets::

    > Ce('Si(32)') # Set mass to 32
    ...

Also, you can work with elements which have charge::

    > Ce('Si2+')
    ...

If you know the atomic number of a element but not the symbol, you can get the
element by its atomic number::

    > Ce(20) # Calcium (Ca)

Converting units
----------------
You can convert between different units with the ``Units`` class::

    > 3 Units.cm
    3 cm
    > (3 Units.cm).to(Units.m)
    0.03 m

.. warning::
    This function is still experimental

Available units:

- Length: Tm, Gm, Mm, km, hm, dam, m, dm, cm, mm, μm, nm, pm
- Volume: like length, but using a ``l``
- Meter squared: like length, but using ``m_2``
- Meter cubic: like length, but using ``m_3``
- Temperature: K, ºC, ºF
- Time: s, min, hour, day
- File size: B, KiB, MiB, GiB, TiB, PiB
