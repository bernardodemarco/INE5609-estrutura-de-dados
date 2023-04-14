from Node import Node


class LinkedList:
    def __init__(self, max_length: int) -> None:
        self.__start = None
        self.__end = None
        self.__max_length = max_length
        self.__num_of_elements = 0

    @property
    def length(self) -> int:
        return self.__num_of_elements

    def is_empty(self) -> bool:
        return self.__num_of_elements == 0

    def is_full(self) -> bool:
        return self.__num_of_elements == self.__max_length

    def insert_at_start(self, value) -> None:
        if self.is_full():
            raise Exception('Linked list is full')

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
        if self.is_full():
            raise Exception('Linked list is full')

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
            raise Exception(
                'Linked list is empty, so the target does not exist in the list')

        if self.is_full():
            raise Exception('Linked list is full')

        fake_node = Node(target)
        self.__end.next = fake_node

        iterator = self.__start
        while iterator.value != target:
            iterator = iterator.next

        self.__end.next = None
        if iterator == fake_node:
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
            raise Exception(
                'Linked list is empty, so the target does not exist in the list')

        if self.is_full():
            raise Exception('Linked list is full')

        iterator = self.__start
        if iterator.value == target:
            return self.insert_at_start(value)

        fake_node = Node(target)
        self.__end.next = fake_node

        while iterator.next.value != target:
            iterator = iterator.next

        if iterator.next == fake_node:
            self.__end.next = None
            raise Exception(
                'The target element that was provided does not exist in the list')

        self.__end.next = None

        node = Node(value)
        node.next = iterator.next
        iterator.next = node
        self.__num_of_elements += 1

    def insert(self, index: int, value) -> None:
        if self.is_full():
            raise Exception('Linked list is full')

        if index < 1 or index > self.__num_of_elements + 1:
            raise Exception('Index out of range')

        if index == 1:
            return self.insert_at_start(value)

        if index == self.__num_of_elements + 1:
            return self.insert_at_end(value)

        iterator = self.__start
        counter = 1
        while counter < index - 1:
            iterator = iterator.next
            counter += 1

        node = Node(value)
        node.next = iterator.next
        iterator.next = node
        self.__num_of_elements += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception('Linked list is empty')

        temp = self.__start

        if self.__num_of_elements == 1:
            self.__start = None
            self.__end = None
            self.__num_of_elements -= 1
            return temp.value

        self.__start = self.__start.next
        self.__num_of_elements -= 1
        return temp.value

    def remove_last(self):
        if self.is_empty():
            raise Exception('Linked list is empty')

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
            raise Exception('Linked list is empty')

        iterator = self.__start
        if iterator.value == target:
            return self.remove_first()

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
            return self.remove_last()

        temp = iterator.next
        iterator.next = iterator.next.next
        self.__num_of_elements -= 1
        return temp.value

    def remove_at_position(self, index: int):
        if index < 1 or index > self.__num_of_elements:
            raise Exception('Index is out of range')

        if index == 1:
            return self.remove_first()

        if index == self.__num_of_elements:
            return self.remove_last()

        iterator = self.__start
        counter = 1
        while counter < index - 1:
            iterator = iterator.next
            counter += 1

        temp = iterator.next
        iterator.next = iterator.next.next
        self.__num_of_elements -= 1
        return temp.value

    def get_first(self):
        if self.is_empty():
            raise Exception('Linked list is empty')

        return self.__start.value

    def get_last(self):
        if self.is_empty():
            raise Exception('Linked list is empty')

        return self.__end.value

    def get_element(self, target):
        if self.is_empty():
            raise Exception('Linked list is empty')

        fake_node = Node(target)
        self.__end.next = fake_node

        iterator = self.__start
        while iterator.value != target:
            iterator = iterator.next

        self.__end.next = None
        if iterator == fake_node:
            raise Exception('The element is not in the linked list')

        return iterator.value

    def get_at_position(self, index: int):
        if index < 1 or index > self.__num_of_elements:
            raise Exception('Index out of range')

        if index == self.__num_of_elements:
            return self.__end.value

        counter = 1
        iterator = self.__start
        while counter < index:
            iterator = iterator.next
            counter += 1

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
