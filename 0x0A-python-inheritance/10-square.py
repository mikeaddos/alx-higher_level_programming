#!/usr/bin/python3
"""rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square"""

    def __init__(self, size):
        """initialize a new square

        Args:
            size (int): The size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
