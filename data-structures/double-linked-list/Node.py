class Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__next = None
        self.__previous = None

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
    def next(self, new_next) -> None:
        self.__next = new_next

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, new_previous) -> None:
        self.__previous = new_previous
