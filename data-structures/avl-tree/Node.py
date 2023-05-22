class Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__left = None
        self.__right = None
        self.__height = 1

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, new_left):
        self.__left = new_left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, new_right):
        self.__right = new_right

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height
