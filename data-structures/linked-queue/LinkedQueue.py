from Node import Node


class LinkedQueue:
    def __init__(self, max_length: int) -> None:
        self.__head = None
        self.__tail = None
        self.__num_of_elements = 0
        self.__max_length = max_length

    def is_empty(self) -> bool:
        return self.__num_of_elements == 0

    def is_full(self) -> bool:
        return self.__num_of_elements == self.__max_length

    def enqueue(self, data) -> None:
        if self.is_full():
            raise Exception('Queue is full')

        node = Node(data)

        if self.is_empty():
            self.__head = node
            self.__tail = node
            self.__num_of_elements += 1
            return

        self.__tail.next = node
        self.__tail = self.__tail.next
        self.__num_of_elements += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        temp = self.__head
        self.__head = self.__head.next
        self.__num_of_elements -= 1
        return temp.value

    def head_element(self) -> Node:
        if self.is_empty():
            raise Exception('Queue is empty')

        return self.__head

    def __str__(self) -> str:
        if self.is_empty():
            return 'HEAD - TAIL (EMPTY QUEUE)'

        queue_str = 'HEAD - '
        node = self.__head
        while node.next is not None:
            queue_str += f'({node.value}) - '
            node = node.next
        queue_str += f'({node.value}) - TAIL'

        return queue_str
