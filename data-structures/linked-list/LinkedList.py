from Node import Node


class LinkedList:
    def __init__(self) -> None:
        self.__start = None
        self.__end = None
        self.__num_of_elements = 0

    @property
    def length(self) -> int:
        return self.__num_of_elements

    def is_empty(self) -> bool:
        return self.__num_of_elements == 0

    def insert_at_start(self, value) -> None:
        node = Node(value)

        if self.is_empty():
            self.__start = node
            self.__end = node
            self.__num_of_elements += 1
            return

        node.next = self.__start
        self.__start = node
        self.__num_of_elements += 1

    def insert_at_end(self, value) -> None:
        node = Node(value)

        if self.is_empty():
            self.__start = node
            self.__end = node
            self.__num_of_elements += 1
            return

        self.__end.next = node
        self.__end = node
        self.__num_of_elements += 1

    def insert_after(self, target, value) -> None:
        if self.is_empty():
            raise Exception('Linked list is empty')

        iterator = self.__start
        while iterator is not None and iterator.value != target:
            iterator = iterator.next

        if iterator is None:
            raise Exception(
                'The target element that was provided does not exist in the list')

        if iterator == self.__end:
            return self.insert_at_end(value)

        node = Node(value)
        node.next = iterator.next
        iterator.next = node
        self.__num_of_elements += 1

    def insert_before(self, target, value) -> None:
        if self.is_empty():
            raise Exception('Linked list is empty')

        iterator = self.__start
        if iterator.value == target:
            return self.insert_at_start(value)

        while iterator.next is not None and iterator.next.value != target:
            iterator = iterator.next

        if iterator.next is None:
            raise Exception(
                'The target element that was provided does not exist in the list')

        node = Node(value)
        node.next = iterator.next
        iterator.next = node
        self.__num_of_elements += 1

    def insert(self, index: int, value) -> None:
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove(self, value):
        pass

    def remove_at_position(self, index: int):
        pass

    def get_first(self):
        if self.is_empty():
            raise Exception('Linked list is empty')

        return self.__start.value

    def get_last(self):
        if self.is_empty():
            raise Exception('Linked list is empty')

        return self.__end.value

    def get_at_position(self, index: int):
        pass

    def __str__(self) -> str:
        if self.is_empty():
            return 'FIRST - LAST (EMPTY LIST)'

        queue_str = 'FIRST - '
        iterator = self.__start
        while iterator is not None:
            queue_str += f'({iterator.value}) - '
            iterator = iterator.next
        queue_str += f'END'

        return queue_str
