from Node import Node


class DoubleLinkedList:
    def __init__(self, max_length: int) -> None:
        self.__start = None
        self.__cursor = None
        self.__max_length = max_length
        self.__num_of_elements = 0

    def __go_forward_k_positions(self, k: int) -> None:
        counter = 0
        while counter < k:
            self.__cursor = self.__cursor.next
            counter += 1

    def __go_back_k_positions(self, k: int) -> None:
        counter = 0
        while counter < k:
            self.__cursor = self.__cursor.previous
            counter += 1

    def __go_to_start(self) -> None:
        self.__cursor = self.__start

    def __go_to_end(self) -> None:
        self.__cursor = self.__start.previous

    def is_empty(self) -> bool:
        return self.__num_of_elements == 0

    def is_full(self) -> bool:
        return self.__num_of_elements == self.__max_length

    def insert_at_start(self, value) -> None:
        pass

    def insert_at_end(self, value) -> None:
        pass

    def insert_before_current(self, value) -> None:
        pass

    def insert_after_current(self, value) -> None:
        pass

    def insert(self, index: int, value) -> None:
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove_element(self, target):
        pass

    def remove_at_position(self, index: int):
        pass

    def remove_current(self):
        pass

    def contains(target) -> bool:
        pass

    def get_current(self):
        pass

    def get_position_of(target) -> int:
        pass
