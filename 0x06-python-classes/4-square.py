#!/usr/bin/python3
""" empty class Square that defines a square """


class Square:
    """ empty class Square """
    def __init__(self, size=0):
        """ attribute:
            size: size os squara.
        """
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ returns the current square area """
        return (self.__size * self.__size)
