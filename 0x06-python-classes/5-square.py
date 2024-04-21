#!/usr/bin/python3
"""Task 5: Printing a square"""


class Square:
    """Geometrical Square Object

    The square have a size attribute which defines the shape of the square,
    the size attribute must be an integer and greater or equal to zero, if not
    errors should arose.
    """
    def __init__(self, size=0):
        """initializing the square instant"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the square area"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square

        print the square in the stdout using # character
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if (self.__size == 0):
            print()
