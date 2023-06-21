class ContinuousDirectory:
    def __init__(self, categories: dict) -> None:
        self.__directory = {}
        self.__categories = categories

    def add_index(self, salary: int, index: int) -> None:
        for (salary_category, salary_interval) in self.__categories.items():
            (min_salary, max_salary) = salary_interval
            if (max_salary is None and salary >= min_salary) or (min_salary <= salary < max_salary):
                if salary_category in self.__directory:
                    self.__directory[salary_category].append(index)
                else:
                    self.__directory[salary_category] = [index]
                break
