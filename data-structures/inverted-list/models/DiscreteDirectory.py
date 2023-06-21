class DiscreteDirectory:
    def __init__(self) -> None:
        self.__directory = {}

    @property
    def directory(self) -> dict:
        return self.__directory

    def add_index(self, key: str, index: int) -> None:
        if key in self.__directory:
            self.__directory[key].append(index)
            return
        self.__directory[key] = [index]
