class ContinuousDirectory:
    def __init__(self, categories: dict) -> None:
        self.__directory = {}
        self.__categories = categories

    def add_index(self, num: int, index: str) -> None:
        for (category, interval) in self.__categories.items():
            (inclusive_min_val, exclusive_max_val) = interval
            if (exclusive_max_val is None and num >= inclusive_min_val) or (inclusive_min_val <= num < exclusive_max_val):
                if category in self.__directory:
                    self.__directory[category].append(index)
                else:
                    self.__directory[category] = [index]
                break
