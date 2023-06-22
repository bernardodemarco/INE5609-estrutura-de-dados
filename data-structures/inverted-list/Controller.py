import json

from constants import JSON_FILE_PATH, SimpleQuery, CompositeQuery

from View import View
from models.InvertedList import InvertedList


class Controller:
    def __init__(self) -> None:
        self.__view = View()
        self.__inverted_list = InvertedList()

    def load_data(self):
        with open(JSON_FILE_PATH) as f:
            self.__inverted_list.data = json.load(f)
            self.__inverted_list.add_data_to_directories()

    def simple_query(self) -> None:
        field = self.__view.show_simple_query_options()
        query = ''
        if field is SimpleQuery.SALARY.value:
            query = self.__view.get_salary_category()
        else:
            query = self.__view.read_answer(message='Digite a busca:')
        indexes = self.__inverted_list.get_simple_query_results(field, query)
        if len(indexes) == 0:
            self.__view.show_message('Nenhum resultado')
        else:
            for index in indexes:
                self.__view.show_student_data({
                    'index': index,
                    **self.__inverted_list.data[index]
                })

    def composite_query(self) -> None:
        fields = self.__view.show_composite_query_options()
        query = {}
        if fields is CompositeQuery.COURSE_AND_SOCCER_TEAM.value:
            course_query = self.__view.read_answer(message='Digite o curso:')
            soccer_team_query = self.__view.read_answer(
                message='Digite o time de futebol:')
            query = {
                'course_query': course_query,
                'soccer_team_query': soccer_team_query
            }
        elif fields is CompositeQuery.COURSE_AND_SALARY.value:
            course_query = self.__view.read_answer(message='Digite o curso:')
            salary_query = self.__view.get_salary_category()
            query = {
                'course_query': course_query,
                'salary_query': salary_query
            }
        else:
            soccer_team_query = self.__view.read_answer(
                message='Digite o time de futebol:')
            salary_query = self.__view.get_salary_category()
            query = {
                'soccer_team_query': soccer_team_query,
                'salary_query': salary_query
            }

        indexes = self.__inverted_list.get_composite_query_results(
            fields, query)

        if len(indexes) == 0:
            self.__view.show_message('Nenhum resultado')
        else:
            for index in indexes:
                self.__view.show_student_data({
                    'index': index,
                    **self.__inverted_list.data[index]
                })

    def insert_element(self):
        try:
            student_data = self.__view.ask_student_data()
            self.__inverted_list.insert_element(student_data)
        except Exception as err:
            self.__view.show_message(err)

    def remove_element(self):
        self.__view.show_message('REMOVER ELEMENTO')
        self.show_data()
        index = self.__view.read_answer(
            message='Digite a matrícula do estudante que você deseja remover:', is_numeric=True)
        try:
            self.__inverted_list.remove_element(index)
        except Exception as err:
            self.__view.show_message(err)

    def show_data(self) -> None:
        for (index, payload) in self.__inverted_list.data.items():
            self.__view.show_student_data({
                'index': index,
                **payload
            })

    def end(self):
        exit(0)

    def run(self):
        switcher = {
            0: self.end,
            1: self.load_data,
            2: self.simple_query,
            3: self.composite_query,
            4: self.insert_element,
            5: self.remove_element,
            6: self.show_data,
        }
        while True:
            switcher[self.__view.show_options()]()
