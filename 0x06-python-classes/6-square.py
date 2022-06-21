#!/usr/bin/python3

""" A class that defines a square """


class Square:
    """A class defining a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """size must be an integer
        size must be greater than or equals zero
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        is_tuple = type(position) != tuple
        if not is_tuple:
            if len(position) == 2:
                x, y = position
                x_type = type(x) != int or x < 0
                y_type = type(y) != int or y < 0
                equals_two = len(position) != 2
            else:
                raise TypeError("position must be a\
                     tuple of 2 positive integers")
        if is_tuple or equals_two or x_type or y_type:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position

    """ getters """
    @property
    def size(self):
        """ returns size """
        return self.__size

    """ setters """
    @size.setter
    def size(self, value):
        """ set size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns area of the square """
        return self.__size**2

    def my_print(self):
        """ returns square"""

        size = self.__size
        position = self.position
        if size == 0:
            print("")
        if position[1] > 0:
            print("\n"*position[0])

        for i in range(size):
            if position[0] > 0:
                print(" "*position[0], end="")
            for j in range(size):
                print("#", end="")
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        is_tuple = type(value) != tuple
        if not is_tuple:
            if len(value) == 2:
                x, y = value
                x_type = type(x) != int or x < 0
                y_type = type(y) != int or y < 0
                equals_two = len(value) != 2
            else:
                raise TypeError("position must be a\
                     tuple of 2 positive integers")
        if is_tuple or equals_two or x_type or y_type:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

