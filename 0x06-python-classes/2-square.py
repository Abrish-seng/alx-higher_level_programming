#!/usr/bin/python3
"""Print integer if not print type error"""

class Square:

    def _init_(self, size = 0):
        self._size = size
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            ValueError("size must be >= 0")
