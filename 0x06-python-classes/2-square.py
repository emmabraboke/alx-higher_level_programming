#!/usr/bin/python3

""" A class that defines a sqaure """


class Square:
    """A class defining a square
    """
    def __init__(self, size):
        """size must be an integer
        size must be greater than or equals zero
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
