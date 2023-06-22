import json

from View import View
from models.InvertedList import InvertedList

FILENAME = 'data.json'


class Controller:
    def __init__(self) -> None:
        self.__view = View()
        self.__inverted_list = InvertedList()

    def load_data(self):
        with open(FILENAME) as f:
            self.__inverted_list.set_data(json.load(f))
            self.__inverted_list.add_data_to_directories()

    def insert_element(self):
        try:
            student_data = self.__view.ask_student_data()
            self.__inverted_list.insert_element(student_data)
        except Exception as err:
            self.__view.show_message(err)

    def end(self):
        exit(0)

    def run(self):
        switcher = {
            0: self.end,
            1: self.load_data,
            4: self.insert_element,
        }
        while True:
            switcher[self.__view.show_options()]()
