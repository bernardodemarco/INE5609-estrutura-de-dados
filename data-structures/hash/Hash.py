from LinkedList import LinkedList


class Hash:
    def __init__(self, table_size: int) -> None:
        self.__table = [None] * table_size
        self.__table_size = table_size

    def __hash(self, key: int) -> int:
        return key % self.__table_size

    def insert(self, value) -> None:
        address = self.__hash(value)

        if self.__table[address] is None:
            self.__table[address] = LinkedList()

        self.__table[address].insert_at_start(value)

    def remove(self, target):
        address = self.__hash(target)
        try:
            return self.__table[address].remove(target)
        except:
            raise Exception('The given element does not exist')

    def get_item(self, target):
        address = self.__hash(target)
        try:
            return self.__table[address].get_element(target)
        except:
            return None

    def print_hash(self) -> None:
        for i in range(self.__table_size):
            print(f'BUCKET = {i}', end=' ')
            print(f'{self.__table[i]}\n')
