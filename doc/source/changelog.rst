Changelog
=========
Current stable `PyPI version <https://pypi.org/project/pyscience/>`_ is 0.3.0

[UNRELEASED] Version 0.4
------------------------

Expected date: about May 1st 2019.

Added
^^^^^
- Add tests.
- Now sessions are saved on disk and you can get expressions typed with
  the up arrow.
- Add python annotations.
- Improve documentation

Changed
^^^^^^^
- PEP8 compatible
- ``:for`` function is now ``:evaluate``. Add support for future interpreter 
  functions.

Deprecated
^^^^^^^^^^

Removed
^^^^^^^

Fixed
^^^^^
- Fix parser error.
- Remove new line on interpreter error.

Version 0.3.0 (March 21st 2019)
-------------------------------

Added
^^^^^
- New pyscience.math functions
- Add better cursor support and sessions with the ``prompt_toolkit``
  library. Now it is a dependency.
- Add support to decimal numbers in the interpreter
- pyscience.datam.Condition now can work with more than one operator
  at same time.
- Now you can get a ChemicalElement by element's name.
- ``units`` module

Changed
^^^^^^^
- Create branches for development. Version 0.3 is located in the ``v0.3``
  branch.
- Improve pyscience.math.number.Expression class
- Improve pyscience.algebra


Version 0.2.0.dev1
------------------
This is a old development version which never will be released.

Added
^^^^^
- New pyscience.math module. Functions:

  * is_even: return if a number is even

  * is_odd: return if a number is odd
  
  * Div: return divisors of a number
  
  * number module:
  
    * Expression: Create expressions.

- Monomial and Polynomial have a new attribute: ``list_of_variables``.
  It returns a list of the variables of each object, without duplicates.
- New pyscience.algebra.equation module: solve first-degree equations.
- Add Variable division by int.
- New ``:eval`` function in the interpreter.

Changed
^^^^^^^
- pyscience.fraction is now at pyscience.math.fraction. This breaks API.
- pyscience.math.fraction.lcm is now at the parent module, pyscience.math.
  This breaks API.
- Changed some names of math functions.
- Changed default Polynomial fraction return type.
- Better ``:for`` errors report.
- Translate API documentation to English.
- Rewrite ``Polynomial.__neg__``
- Rewrite ``Polynomial.__str__``

Fixed
^^^^^
- Fix error multiplying a Variable by a Polynomial
- Fix error multiplying a Polynomial by a Monomial
- Fix error subtracting a Monomial from a int
- Fix Polynomial division

Version 0.1.0.dev4 (February 20th 2019)
---------------------------------------
- Initial release.

