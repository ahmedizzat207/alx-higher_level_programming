#!/usr/bin/python3
"""Task 3: Area of a square

Add a method area to obtain the current area of the square instance
"""


class Square:
    """Geometrical square object

    The square have a specific size which added in the instance creation, this
    size argument should be an integer and greater or equal to zero, otherwise
    Errors will arose.
    """
    def __init__(self, size=0):
        """Validate the size parameter"""
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
