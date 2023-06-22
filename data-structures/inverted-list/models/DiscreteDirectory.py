class DiscreteDirectory:
    def __init__(self) -> None:
        self.__directory = {}

    @property
    def directory(self) -> dict:
        return self.__directory

    def get_indexes(self, query: str) -> list:
        print(query)
        if query not in self.__directory:
            return []

        return self.__directory[query]

    def add_index(self, key: str, index: str) -> None:
        if key in self.__directory:
            self.__directory[key].append(index)
            return
        self.__directory[key] = [index]

    def remove_index(self, key: str, index: str) -> None:
        self.__directory[key].remove(index)
