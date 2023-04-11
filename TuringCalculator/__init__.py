# TURING CALCULATOR
# ----------------------------------------------------------------------------------------------------------------
"""
    A simple calculator that can perform the following operations:

    - Addition: add two numbers and return the result.
    - Subtraction: subtract two numbers and return the result.
    - Multiplication: multiply two numbers and return the result.
    - Division: divide two numbers and return the result.
    - Find root: take the n-th root of a number and return the result.
    - Reset memory: reset the calculator's memory to 0.
"""

__version__ = "0.0.1"


# START --------
import doctest


# EXECUTION ----
class Calculator(object):
    """
    A simple calculator that can perform the following operations:

    - Addition: add two numbers and return the result.
    - Subtraction: subtract two numbers and return the result.
    - Multiplication: multiply two numbers and return the result.
    - Division: divide two numbers and return the result.
    - Find root: take the n-th root of a number and return the result.
    - Reset memory: reset the calculator's memory to 0.

    Usage: an instance of Calculator takes 1 optional argument as the default value.

    - To perform an operation, call the relevant method on the instance.
    - To access the result of the previous operation, use the 'getResult' method.
    - To reset the calculator's memory to 0, use the `resetMemory` method.

    Example usage:

    >>> calculator = Calculator()
    >>> calculator.add(9)
    >>> calculator.getResult()
    9
    >>> calculator.subtract(5)
    >>> calculator.getResult()
    4
    >>> calculator.multiply(6)
    >>> calculator.getResult()
    24
    >>> calculator.divided(3)
    >>> calculator.getResult()
    8.0
    >>> calculator.root(3)
    >>> calculator.getResult()
    2.0
    >>> calculator.reset()
    >>> calculator.getResult()
    0
    """

    def __init__(self, default=0):
        self.__value = default
        
    def getResult(self):
        """
        Usage: get current value in memory
        """
        return self.__value

    def add(self, term):
        """
        Usage: increase current value by <term>
        """
        self.__value += term

    def subtract(self, term):
        """
        Increase current value by <term>
        """
        self.__value -= term

    def multiply(self, factor):
        """
        Usage: find the  current value by <term>
        """
        self.__value *= factor

    def divided(self, divisor):
        """
        Usage: divide current value by <divisor>
        """
        self.__value /= divisor

    def root(self, degree):
        """
        Usage: find the <degree>-th root of current value
        """
        self.__value **= 1/degree

    def reset(self):
        """
        Usage: reset the calculator
        """
        self.__value = 0


# END ----------
if __name__ == '__main__':
    print(doctest.testmod())
