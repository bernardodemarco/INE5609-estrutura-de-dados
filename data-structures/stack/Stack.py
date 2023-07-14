class Stack:
    def __init__(self, max_length: int) -> None:
        self.__stack = [0] * max_length
        self.__top = -1
        self.__max_length = max_length

    @property
    def stack(self) -> list:
        ''' stack getter method '''
        return self.__stack[:self.__top + 1]

    def is_empty(self) -> bool:
        ''' Returns a boolean indicating whether the stack is empty or not '''
        return self.__top == -1

    def is_full(self) -> bool:
        ''' Returns a boolean indicating whether the stack is full or not '''
        return self.__top == self.__max_length - 1

    def push(self, data: int) -> None:
        ''' Pushes a given element into the stack '''
        if self.is_full():
            raise Exception('Stack is full')

        self.__top += 1
        self.__stack[self.__top] = data

    def pop(self) -> int:
        ''' Removes the last element of the stack  '''
        if self.is_empty():
            raise Exception('Stack is empty')

        self.__top -= 1
        return self.__stack[self.__top + 1]

    def top(self) -> int:
        ''' Returns the element that is on the top of the stack '''
        if self.is_empty():
            raise Exception('Stack is empty')

        return self.__stack[self.__top]

    def __str__(self) -> str:
        ''' Returns a string representation of the stack '''
        if self.is_empty():
            return '[]\n' * self.__max_length

        stack_representation = ''
        if not self.is_full():
            stack_representation += '[]\n' * \
                (self.__max_length - self.__top - 1)

        for i in range(self.__top, -1, -1):
            stack_representation += f'[{self.__stack[i]}]\n'

        return stack_representation
