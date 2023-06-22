from DiscreteDirectory import DiscreteDirectory
from ContinuousDirectory import ContinuousDirectory

SALARY_CATEGORIES = {
    '''
        Each salary category maps to an interval, in which the first
        value is inclusive and the second one is exclusive.
        For example: [first_value; second_value[
        "None" means +(infinite).
    '''
    'beginner_salary': (0, 5000),
    'intermediate_salary': (5000, 10000),
    'advanced_salary': (10000, None)
}


class InvertedList:
    def __init__(self) -> None:
        self.__data = {}
        self.__course_directory = DiscreteDirectory()
        self.__soccer_team_directory = DiscreteDirectory()
        self.__salary_directory = ContinuousDirectory(SALARY_CATEGORIES)

    @property
    def data(self) -> dict:
        return self.__data

    @data.setter
    def data(self, new_data: dict) -> None:
        self.__data = new_data

    def add_data_to_directories(self, data_to_add=None) -> None:
        data = self.__data
        if data_to_add is not None:
            data = data_to_add

        for (index, payload) in data.items():
            self.__course_directory.add_index(payload['course'], index)
            self.__soccer_team_directory.add_index(
                payload['soccer_team'], index)
            self.__salary_directory.add_index(payload['salary'], index)

    def insert_element(self, raw_data: dict) -> None:
        if raw_data['index'] in self.__data:
            raise Exception('Element already exists')

        index = raw_data['index']
        payload = {
            'name': raw_data['name'],
            'course': raw_data['course'],
            'soccer_team': raw_data['soccer_team'],
            'salary': raw_data['salary']
        }
        self.__data[index] = payload
        self.add_data_to_directories({
            index: payload
        })
