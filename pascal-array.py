# Implementation of the Pascal array
# Example 1 ->
# type
#    arr = array [-2 .. 2] of real;
# Type arr would me an array with five elements,
# starting at index -2 and finishing at index 2.
# arr: [el, el, el, el, el]
#        indexes: [-2, -1, 0, 1, 2]
# Example 2 ->
# type
#    arr = array [7 .. 5] of real;
# indexes: [7, 6, 5]
# PascalArray implementation:
# Example 1 -> PascalArray(-2, 2)
# Example 2 -> PascalArray(7, 5)

class PascalArray:
    def __init__(self, lower_index: int, upper_index: int) -> None:
        if not isinstance(lower_index, int) or not isinstance(upper_index, int):
            raise Exception('Array indexes must be of type int')

        self.__sorted_index = lower_index < upper_index
        self.__upper_index = max(lower_index, upper_index)
        self.__lower_index = min(lower_index, upper_index)
        self.__max_length = self.__upper_index - self.__lower_index + 1
        self.__array = [0] * self.__max_length
        self.__num_of_elements = 0

    @property
    def array(self) -> list:
        ''' array getter method '''
        return self.__array

    def is_empty(self) -> bool:
        ''' Returns a boolean indicating whether the array is empty or not '''
        return self.__num_of_elements == 0

    def is_out_of_range(self, index: int) -> bool:
        ''' Returns a boolean indicating whether the index is inside the array's range '''
        return not self.__lower_index <= index <= self.__upper_index

    def get(self, index: int) -> int:
        ''' Returns the element at the position <index> '''
        if self.is_empty():
            raise Exception('Array is empty')

        if self.is_out_of_range(index):
            raise Exception('Index out of range')

        if not isinstance(index, int):
            raise Exception('Array indexes must be of type int')

        if not self.__sorted_index:
            return self.__array[abs(index - self.__upper_index)]

        return self.__array[index - self.__lower_index]

    def set(self, index: int, data: int) -> None:
        ''' Sets a given number at the position <index> '''
        if self.is_out_of_range(index):
            raise Exception('Index out of range')

        if not isinstance(index, int):
            raise Exception('Array indexes must be of type int')

        self.__num_of_elements += 1
        if not self.__sorted_index:
            self.__array[abs(index - self.__upper_index)] = data
        else:
            self.__array[index - self.__lower_index] = data
