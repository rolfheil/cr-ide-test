"""
Simple math routines
"""


def factorial(n):
    """ Computes the factorial of n.

           Parameters
           ----------
           n: integer


           Returns
           -------
           int
               n! for non-negative numbers n
    """
    if n <= 0:
        return 1
    return n * factorial(n-1)