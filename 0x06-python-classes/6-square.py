#!/usr/bin/python3
""" empty class Square that defines a square """


class Square:
    """ empty class Square """

    def __init__(self, size=0, position=(0, 0)):
        """ attribute:
            size: size os squara.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value1):
        if isinstance((value1, tuple) and len(value1) == 2 and
                all(isinstance(x, int) for x in value1) and
                all(x > 0 for x in value1)):
            self.__position = value1
        else:
            TypeError("position must be a tuple of 2 positive integers")
        
    def area(self):
        """ returns the current square area """
        return (self.__size * self.__size)

    def my_print(self):
        """ hat prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            if self.__position[0] > 0:
                for x in range(self.__position[0]):
                    print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print()
