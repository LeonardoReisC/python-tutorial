"""Documentation

    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 
    1500s, when an unknown printer took a galley of type and scrambled it to 
    make a type specimen book.
"""
class Foo:
    """Class Foo

    Thats a class documentation using docStrings
    """

def sum(x: int | float, y: int | float) -> int | float:
    """ Sums x and y

    Thats a function documentation using docStrings

    :param x: first number
    :type x: int or float
    :param y: second number
    :type y: int or float

    :return the sum of x and y
    :rtype: int or float
    """
    return x + y

a = 'var1'
b = 'var2'
c = 'var3'
d = 'var4'

# print(dir()): shows the obejct(module) attributes 

help(__name__)