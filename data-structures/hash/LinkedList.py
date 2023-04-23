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
    def next(self, new_next) -> None:
        self.__next = new_next


class LinkedList:
    def __init__(self) -> None:
        self.__start = None
        self.__end = None
        self.__num_of_elements = 0

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

    def __remove_first(self):
        temp = self.__start

        if self.__num_of_elements == 1:
            self.__start = None
            self.__end = None
            self.__num_of_elements -= 1
            return temp.value

        self.__start = self.__start.next
        self.__num_of_elements -= 1
        return temp.value

    def __remove_last(self):
        temp = self.__end

        if self.__num_of_elements == 1:
            self.__start = None
            self.__end = None
            self.__num_of_elements -= 1
            return temp.value

        counter = 1
        iterator = self.__start
        while counter < self.__num_of_elements - 1:
            iterator = iterator.next
            counter += 1

        iterator.next = None
        self.__end = iterator
        self.__num_of_elements -= 1
        return temp.value

    def remove(self, target):
        if self.is_empty():
            raise Exception('List is empty')

        iterator = self.__start
        if iterator.value == target:
            return self.__remove_first()

        fake_node = Node(target)
        self.__end.next = fake_node

        while iterator.next.value != target:
            iterator = iterator.next

        if iterator.next == fake_node:
            self.__end.next = None
            raise Exception(
                'The target element that was provided does not exist in the list')

        self.__end.next = None

        if iterator.next == self.__end:
            return self.__remove_last()

        temp = iterator.next
        iterator.next = iterator.next.next
        self.__num_of_elements -= 1
        return temp.value

    def get_element(self, target):
        if self.is_empty():
            raise Exception('List is empty')

        fake_node = Node(target)
        self.__end.next = fake_node

        iterator = self.__start
        while iterator.value != target:
            iterator = iterator.next

        self.__end.next = None
        if iterator == fake_node:
            raise Exception('The element is not in the linked list')

        return iterator.value

    def __str__(self) -> str:
        if self.is_empty():
            return 'START - END (EMPTY LIST)'

        list_str = 'START - '
        iterator = self.__start
        while iterator is not None:
            list_str += f'({iterator.value}) - '
            iterator = iterator.next
        list_str += f'END'

        return list_str
