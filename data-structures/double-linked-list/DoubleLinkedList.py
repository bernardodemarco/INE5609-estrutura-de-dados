from Node import Node


class DoubleLinkedList:
    def __init__(self, max_length: int) -> None:
        """
        The constructor for DoubleLinkedList class.

        Args:
            max_length (int): maximum length of the list.

        Raises:
            Exception: if max_length is not a number or if it is less than 1.
        """
        self.__start = None
        self.__cursor = None
        self.__num_of_elements = 0
        if isinstance(max_length, int) and max_length > 0:
            self.__max_length = max_length
        else:
            raise Exception(
                'max_length parameter must be an integer greater than zero')

    def __go_forward_k_positions(self, k: int) -> None:
        """
        Offset cursor k positions forward.

        Args:
            k (int): number of positions to offset the cursor.
        """
        counter = 0
        while counter < k:
            self.__cursor = self.__cursor.next
            counter += 1

    def __go_backward_k_positions(self, k: int) -> None:
        """
        Offset cursor k positions backwards.

        Args:
            k (int): number of positions to offset the cursor.
        """
        counter = 0
        while counter < k:
            self.__cursor = self.__cursor.previous
            counter += 1

    def __go_to_start(self) -> None:
        """Move cursor to the start of the list."""
        self.__cursor = self.__start

    def __go_to_end(self) -> None:
        """Move cursor to then end of the list."""
        self.__cursor = self.__start.previous

    def is_empty(self) -> bool:
        """Return a boolean indicating whether the list is empty or not."""
        return self.__num_of_elements == 0

    def is_full(self) -> bool:
        """Return a boolean indicating whether the list is full or not."""
        return self.__num_of_elements == self.__max_length

    def __handle_insertion_with_empty_list(self, value) -> None:
        """
        Insert element when the list is empty.

        Args:
            value: element to be inserted.
        """
        node = Node(value)
        self.__start = node
        self.__cursor = node
        node.previous = node
        node.next = node
        self.__num_of_elements += 1

    def insert_before_current(self, value) -> None:
        """
        Insert element before list's current element (cursor).

        Args:
            value: element to be inserted.

        Raises:
            Exception: if list is full or empty.
        """
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
        """
        Insert element after list's current element (cursor).

        Args:
            value: element to be inserted.

        Raises:
            Exception: if list is full or empty.
        """
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
        """
        Insert element at the start of the list.

        Args:
            value: element to be inserted.

        Raises:
            Exception: if list is full.
        """
        if self.__num_of_elements == 0:
            return self.__handle_insertion_with_empty_list(value)

        self.__go_to_start()
        self.insert_before_current(value)

    def insert_at_end(self, value) -> None:
        """
        Insert element at the end of the list.

        Args:
            value: element to be inserted.

        Raises:
            Exception: if list is full.
        """
        if self.__num_of_elements == 0:
            return self.__handle_insertion_with_empty_list(value)

        self.__go_to_end()
        self.insert_after_current(value)

    def insert_at_position(self, index: int, value) -> None:
        """
        Insert element at a given index in the list.

        Args:
            index (int): position to insert the element in.
            value: element to be inserted.

        Raises:
            Exception: if index is less than one or greater than the list's length plus one.
        """
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
        """
        Remove the current element. 

        Remove the current element. Once it has been removed, the list's 
        current element becomes the previous element of the removed element.
        However, if the element that was removed was the list's first element,
        then the list's current element will be the next element of the removed one.

        Returns:
            element that has been removed.

        Raises:
            Exception: if list is empty.
        """
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
            self.__go_backward_k_positions(1)

        return temp.value

    def remove_first(self):
        """
        Remove the first element of the list. The list's current element becomes the next element of the removed one.

        Returns:
            element that has been removed.

        Raises:
            Exception: if list is empty.
        """
        if self.is_empty():
            raise Exception(
                'List is empty, so there is no element to be removed')

        self.__go_to_start()
        return self.remove_current()

    def remove_last(self):
        """
        Remove the last element of the list. The list's current element becomes the previous element of the removed one.

        Returns:
            element that has been removed.

        Raises:
            Exception: if list is empty.
        """
        if self.is_empty():
            raise Exception(
                'List is empty, so there is no element to be removed')

        self.__go_to_end()
        return self.remove_current()

    def remove_element(self, target):
        """
        Remove element that was passed as parameter.

        Once it has been removed, the list's current element becomes the previous
        element of the removed element. However, if the element that was removed was
        the list's first element, then the list's current element will be the next element of the removed one.

        Args:
            target: element to be removed.

        Returns:
            element that has been removed.

        Raises:
            Exception: if element is not in the list.
        """
        if not self.contains(target):
            raise Exception('The given element does not exist in the list')

        return self.remove_current()

    def remove_at_position(self, index: int):
        """
        Remove element at a given position from the list.

        Once it has been removed, the list's current element becomes the previous
        element of the removed element. However, if the element that was removed was
        the list's first element, then the list's current element will be the next element of the removed one.

        Args:
            index (int): position of the element to be removed.

        Returns:
            element that has been removed.

        Raises:
            Exception: if index is less than one or greater than the number of elements.
        """
        if index < 1 or index > self.__num_of_elements:
            raise Exception('Index out of range')

        if index == 1:
            return self.remove_first()

        if index == self.__num_of_elements:
            return self.remove_last()

        self.__go_to_start()
        self.__go_forward_k_positions(index - 1)
        return self.remove_current()

    def contains(self, target) -> bool:
        """
        Check if a given element is in the list.

        If the element is in the list, it will become the list's current element. 
        If it is not, then the list's current element will be the first element.

        Args:
            target: element to be searched for in the list.

        Returns:
            bool: boolean value indicating whether the element is in the list or not.
        """
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
        """Return the current element."""
        if self.is_empty():
            raise Exception('List is empty')

        return self.__cursor.value

    def get_position_of(self, target) -> int:
        """
        Get the position of a given element is in the list.

        Args:
            target: element to be searched for in the list.

        Returns:
            int: position of the given element in the list.

        Raises:
            Exception: if list is empty or the element does not exist in the list.
        """
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
        """Return the element that is at the start of the list."""
        if self.is_empty():
            raise Exception('List is empty')

        return self.__start.value

    def get_end(self):
        """Return the element that is at the end of the list."""
        if self.is_empty():
            raise Exception('List is empty')

        return self.__start.previous.value

    def get_length(self) -> int:
        """Return the length of the list."""
        return self.__num_of_elements

    def print_list(self) -> None:
        """Print the list."""
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
