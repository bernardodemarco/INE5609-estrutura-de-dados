from Node import Node


class DoubleLinkedList:
    def __init__(self, max_length: int) -> None:
        self.__start = None
        self.__cursor = None
        self.__num_of_elements = 0
        if isinstance(max_length, int) and max_length > 0:
            self.__max_length = max_length
        else:
            raise Exception(
                'max_length parameter must be an integer greater than zero')

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

    def __handle_insertion_with_empty_list(self, value) -> None:
        node = Node(value)
        self.__start = node
        self.__cursor = node
        node.previous = node
        node.next = node
        self.__num_of_elements += 1

    def insert_before_current(self, value) -> None:
        if self.is_full():
            raise Exception('List is full')

        if self.is_empty():
            raise Exception(
                'List is empty, so it is not possible to insert before current')

        node = Node(value)
        node.next = self.__cursor
        node.previous = self.__cursor.previous
        self.__cursor.previous.next = node
        self.__cursor.previous = node
        self.__num_of_elements += 1

        if self.__cursor == self.__start:
            self.__start = self.__cursor.previous

    def insert_after_current(self, value) -> None:
        if self.is_full():
            raise Exception('List is full')

        if self.is_empty():
            raise Exception(
                'List is empty, so it is not possible to insert after current')

        node = Node(value)
        node.next = self.__cursor.next
        node.previous = self.__cursor
        self.__cursor.next.previous = node
        self.__cursor.next = node
        self.__num_of_elements += 1

    def insert_at_start(self, value) -> None:
        if self.__num_of_elements == 0:
            return self.__handle_insertion_with_empty_list(value)

        self.__go_to_start()
        self.insert_before_current(value)

    def insert_at_end(self, value) -> None:
        if self.__num_of_elements == 0:
            return self.__handle_insertion_with_empty_list(value)

        self.__go_to_end()
        self.insert_after_current(value)

    def insert(self, index: int, value) -> None:
        if index < 1 or index > self.__num_of_elements + 1:
            raise Exception('Index out of range')

        if index == 1:
            return self.insert_at_start(value)

        if index == self.__num_of_elements + 1:
            return self.insert_at_end(value)

        self.__go_to_start()
        self.__go_forward_k_positions(index - 1)
        self.insert_before_current(value)

    def remove_current(self):
        if self.is_empty():
            raise Exception(
                'List is empty, so there is no element to be removed')

        temp = self.__cursor

        if self.__num_of_elements == 1:
            self.__start = None
            self.__cursor = None
            self.__num_of_elements -= 1
            return temp.value

        self.__cursor.previous.next = self.__cursor.next
        self.__cursor.next.previous = self.__cursor.previous
        self.__num_of_elements -= 1

        if self.__cursor == self.__start:
            self.__start = self.__cursor.next
            self.__go_forward_k_positions(1)
        else:
            self.__go_back_k_positions(1)

        return temp.value

    def remove_first(self):
        self.__go_to_start()
        return self.remove_current()

    def remove_last(self):
        self.__go_to_end()
        return self.remove_current()

    def remove_element(self, target):
        if not self.contains(target):
            raise Exception('The given element does not exist in the list')

        return self.remove_current()

    def remove_at_position(self, index: int):
        if index < 1 or index > self.__num_of_elements:
            raise Exception('Index out of range')

        self.__go_to_start()
        self.__go_forward_k_positions(index - 1)
        return self.remove_current()

    def contains(self, target) -> bool:
        if self.is_empty():
            return False

        self.__go_to_start()
        fake_node = Node(target)
        self.__start.previous.next = fake_node

        while self.__cursor.value != target:
            self.__cursor = self.__cursor.next

        self.__start.previous.next = self.__start
        if self.__cursor == fake_node:
            self.__go_to_start()
            return False

        return True

    def get_current(self):
        if self.is_empty():
            raise Exception('List is empty')

        return self.__cursor.value

    def get_position_of(self, target) -> int:
        if self.is_empty():
            raise Exception('List is empty')

        self.__go_to_start()
        fake_node = Node(target)
        self.__start.previous.next = fake_node

        position = 1
        while self.__cursor.value != target:
            self.__cursor = self.__cursor.next
            position += 1

        self.__start.previous.next = self.__start
        if self.__cursor == fake_node:
            self.__go_to_start()
            raise Exception('The given element does not exist in the list')

        return position

    def get_start(self):
        if self.is_empty():
            raise Exception('List is empty')

        return self.__start.value

    def get_end(self):
        if self.is_empty():
            raise Exception('List is empty')

        return self.__start.previous.value

    def get_length(self) -> int:
        return self.__num_of_elements

    def print_list(self) -> None:
        if self.is_empty():
            print('START - END (EMPTY LIST)')
            return

        list_str = 'START - '
        self.__go_to_start()
        while self.__cursor.next != self.__start:
            list_str += f'({self.__cursor.value}) - '
            self.__cursor = self.__cursor.next
        list_str += f'({self.__cursor.value}) - END\n'

        print(list_str)
