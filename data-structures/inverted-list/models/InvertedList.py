from models.DiscreteDirectory import DiscreteDirectory
from models.ContinuousDirectory import ContinuousDirectory

from constants import SALARY_CATEGORIES, SimpleQuery, CompositeQuery


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

    def get_simple_query_results(self, field: int, query: str) -> list:
        if field is SimpleQuery.COURSE.value:
            return self.__course_directory.get_indexes(query)

        if field is SimpleQuery.SOCCER_TEAM.value:
            return self.__soccer_team_directory.get_indexes(query)

        return self.__salary_directory.get_indexes(query)

    def get_composite_query_results(self, fields: int, query: dict) -> list:
        if fields is CompositeQuery.COURSE_AND_SOCCER_TEAM.value:
            course_indexes = self.__course_directory.get_indexes(
                query['course_query'])
            soccer_team_indexes = self.__soccer_team_directory.get_indexes(
                query['soccer_team_query'])
            return list(set(course_indexes) & set(soccer_team_indexes))

        if fields is CompositeQuery.COURSE_AND_SALARY.value:
            course_indexes = self.__course_directory.get_indexes(
                query['course_query'])
            salary_indexes = self.__salary_directory.get_indexes(
                query['salary_query'])
            return list(set(course_indexes) & set(salary_indexes))

        soccer_team_indexes = self.__soccer_team_directory.get_indexes(
            query['soccer_team_query'])
        salary_indexes = self.__salary_directory.get_indexes(
            query['salary_query'])
        return list(set(soccer_team_indexes) & set(salary_indexes))

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

    def remove_element(self, index: str) -> None:
        if index not in self.__data:
            raise Exception('Element does not exist')

        removed_element = self.__data.pop(index)
        self.__course_directory.remove_index(removed_element['course'], index)
        self.__soccer_team_directory.remove_index(
            removed_element['soccer_team'], index)
        self.__salary_directory.remove_index(removed_element['salary'], index)
