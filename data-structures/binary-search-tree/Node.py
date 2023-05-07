class Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__right = None
        self.__left = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, new_right):
        self.__right = new_right

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, new_left):
        self.__left = new_left
