class Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value) -> None:
        self.__value = new_value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next):
        self.__next = new_next
