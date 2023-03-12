class Queue:
    def __init__(self, max_length: int) -> None:
        self.__max_length = max_length
        self.__queue = [0] * max_length
        self.__head = 0
        self.__tail = -1
        self.__num_of_elements = 0

    @property
    def queue(self) -> list:
        ''' queue getter method '''
        if self.__num_of_elements == 0:
            return []
        return self.__queue[self.__head: self.__tail + 1]

    def is_empty(self) -> bool:
        ''' Returns a boolean indicating whether the queue is empty or not '''
        return self.__num_of_elements == 0

    def is_full(self) -> bool:
        ''' Returns a boolean indicating whether the queue is empty or not '''
        return self.__num_of_elements == self.__max_length

    def enqueue(self, data: int) -> None:
        ''' Inserts value in the end (tail) of the queue '''
        if self.is_full():
            raise Exception('Queue is full')

        # Incrementing tail using mod division handles
        # situations where (tail == max_length - 1) and it'll
        # be incremented
        self.__tail = (1 + self.__tail) % self.__max_length
        self.__queue[self.__tail] = data
        self.__num_of_elements += 1

    def dequeue(self) -> int:
        ''' Removes the first value that entered in the queue '''
        if self.is_empty():
            raise Exception('Queue is empty')

        # Incrementing head using mod division handles
        # situations where (head == max_length - 1) and it'll
        # be incremented
        self.__head = (1 + self.__head) % self.__max_length
        self.__num_of_elements -= 1
        return self.__queue[self.__head - 1]

    def head_element(self) -> int:
        ''' Returns the first value on the queue '''
        if (self.is_empty()):
            raise Exception('Queue is empty')
        return self.__queue[self.__head]

    def __str__(self) -> str:
        ''' Returns a string representation of the queue '''
        if self.is_empty():
            return 'HEAD - TAIL (empty queue)'

        queue_str = 'HEAD - '
        for i in range(self.__head, self.__tail + 1):
            queue_str += f'({self.__queue[i]}) - '
        return queue_str + 'TAIL'
