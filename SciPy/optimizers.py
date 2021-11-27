"""
SciPy Optimizers

Optimizers are a set of procedures defined in SciPy that either find
the minimum value of a function, or the root of an equation.

Optimizing Functions

Essentially, all of the algorithms in Machine Learning are nothing more
than a complex equation that needs to be minimized with the help of given data.

Roots of an Equation

NumPy is capable of finding roots for polynomials and linear equations,
but it can not find roots for non linear equations, like this one:

x + cos(x)

For that you can use SciPy's << optimze.root >> function.
This function takes two required arguments:

fun  - a function representing an equation.
x0  - an initial guess for the root.

The function returns an object with information regarding the solution.
The actual solution is given under attribute x of the returned object:
Example: Find root of the equation x + cos(x):
"""
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(0)

myroot = root(eqn, 0)

print (myroot.x)

print()
"""
Note: The returned object has much more information about the solution.
Example: Print all information about the solution (not just x which is the root)
"""
print (myroot)  #this returns an object that gives us more information

print()
"""
The equation is two expressions separated by an equal sign (=).
We will mainly deal with equations that contain one or more variables.
Roots of the equation are such values of the variable,
that turn equation into correct equality.
Determine, whether 2 and 3 are roots of the equation 15=x**2+2x
To check it, we just plug values instead of the variable.

Check for 2:  15=2**2 + 2⋅2

                15≠8

We haven't obtained correct equality, so 2 is not root of the equation.

Check for 3: 15=3**2 + 2⋅3

                15=15

Since equality is correct, then 3 is root of the equation.
"""
"""
Minimizing a Function

A function, in this context, represents a curve, curves have high points and low points.

High points are called maxima.
Low points are called minima.

The highest point in the whole curve is called global maxima,
whereas the rest of them are called local maxima.

The lowest point in whole curve is called global minima,
whereas the rest of them are called local minima.

Finding Minima

We can use << scipy.optimize.minimize() >> function to minimize the function.
The << minimize() >> function takes the following arguments:

fun  - a function representing an equation.
x0  - an initial guess for the root.
method  - name of the method to use. Legal values:
    'CG'
    'BFGS'
    'Newton-CG'
    'L-BFGS-B'
    'TNC'
    'COBYLA'
    'SLSQP'

callback -  function called after each iteration of optimization.

options -  a dictionary defining extra params:
{
     "disp": boolean - print detailed description
     "gtol": number - the tolerance of the error
  }

Example: Minimize the function x^2 + x + 2 with BFGS:
"""
from scipy.optimize import minimize

def eqn(x):
    return x**2 + x + 2

mymin = minimize(eqn, 0, method = 'BFGS')

print (mymin)
