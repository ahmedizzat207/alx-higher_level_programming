#!/usr/bin/python3
"""Task 6: Coordinates of a square"""


class Square:
    """Geometrical Square Object

    The square has a size attribute which should be an integer and greater or
    equal to zero.
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializing the square instant"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and
           len(value) == 2 and
           isinstance(value[0], int) and
           isinstance(value[1], int) and
           value[0] >= 0 and
           value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculate the square area

        Square area = (square size) ** 2
        """
        return (self.__size ** 2)

    def my_print(self):
        """print the square using # character

        Example:
            a square of size 2 would be like this:
                $##
                $##
            the position attribute identify how to print the square, the first
            parameter of the position tuple identifies the number of speaces
            should be printed before each row of the square, and the second
            parameter of position signifies the number of line printed before
            printing the square, for example for a position value = (2, 1)
            the printed square will be like this:
                $
                $  ##
                $  ##
        """
        if (self.__size == 0):
            print()
            return
        for newline in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
