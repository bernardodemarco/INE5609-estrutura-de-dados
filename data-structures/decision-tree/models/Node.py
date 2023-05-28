class Node:
    def __init__(self, value: str) -> None:
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, new_value: str) -> None:
        self.__value = new_value
