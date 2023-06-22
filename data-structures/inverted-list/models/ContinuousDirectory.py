class ContinuousDirectory:
    def __init__(self, categories: dict) -> None:
        self.__directory = {}
        self.__categories = categories

    def get_category(self, num: int) -> str:
        for (category, interval) in self.__categories.items():
            (inclusive_min_val, exclusive_max_val) = interval
            if (exclusive_max_val is None and num >= inclusive_min_val) or (inclusive_min_val <= num < exclusive_max_val):
                return category

    def get_indexes(self, category: str) -> list:
        if category not in self.__directory:
            return []

        return self.__directory[category]

    def add_index(self, num: int, index: str) -> None:
        category = self.get_category(num)
        if category in self.__directory:
            self.__directory[category].append(index)
        else:
            self.__directory[category] = [index]

    def remove_index(self, num: int, index: str) -> None:
        category = self.get_category(num)
        self.__directory[category].remove(index)
