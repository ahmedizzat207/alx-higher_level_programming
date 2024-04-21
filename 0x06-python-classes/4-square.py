#!/usr/bin/python3
"""Task 4: Access and update private attribute"""


class Square:
    """Geometrical Square Object

    The square will have a size attribute that should be integer and greater
    or eqaul to zero, if not errors should arose.
    """
    def __init__(self, size=0):
        """set and validate size attribute using property and setter"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return (self.__size ** 2)
