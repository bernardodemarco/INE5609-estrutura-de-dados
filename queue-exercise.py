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
        return self.__queue

    def is_empty(self) -> bool:
        ''' Returns a boolean indicating whether the queue is empty or not '''
        return self.__num_of_elements == 0

    def is_full(self) -> bool:
        ''' Returns a boolean indicating whether the queue is full or not '''
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

        # Temporary variable to store the removed item.
        # In Python, without this, just by returning
        # self.__queue[self.__head - 1] it would work fine,
        # but in other languages it would not.
        # For instance, imagine that head == max_length - 1,
        # then head is incremented by one, becoming zero (mod division).
        # If you accessed self.__queue[self.__head - 1],
        # then you would receive an error (index == -1).
        temp = self.__queue[self.__head]

        # Incrementing head using mod division handles
        # situations where (head == max_length - 1) and it'll
        # be incremented
        self.__head = (1 + self.__head) % self.__max_length
        self.__num_of_elements -= 1
        return temp

    def head_element(self) -> int:
        ''' Returns the first value on the queue '''
        if self.is_empty():
            raise Exception('Queue is empty')

        return self.__queue[self.__head]
