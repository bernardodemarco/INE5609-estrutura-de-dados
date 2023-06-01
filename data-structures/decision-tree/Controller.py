import pickle
from View import View
from DecisionTree import DecisionTree
from Node import Node
from enums import Answer, Direction

FILENAME = 'tree-data.pkl'


class Controller:
    def __init__(self) -> None:
        self.__view = View()
        self.__tree = None
        try:
            self.__tree = self.__load()
        except FileNotFoundError:
            self.__tree = DecisionTree('Chapecoense')

    def __load(self):
        with open(FILENAME, 'rb') as f:
            return pickle.load(f)

    def __dump(self):
        with open(FILENAME, 'wb') as f:
            pickle.dump(self.__tree, f)

    def play_game(self):
        self.__view.show_message('Pense em um time de futebol!')

        iterator = self.__tree.root
        parent = None
        direction = None

        while not iterator.is_leaf():
            answer = self.__view.ask_question(iterator.value)
            parent = iterator
            if answer == Answer.YES.value:
                direction = Direction.CORRECT_ANSWER
                iterator = iterator.yes
            elif answer == Answer.NO.value:
                direction = Direction.WRONG_ANSWER
                iterator = iterator.no

        answer = self.__view.guess_answer(iterator.value)
        if answer == Answer.YES.value:
            self.end_game()
        elif answer == Answer.NO.value:
            (new_team, new_question) = self.__view.ask_difference(iterator.value)

            new_question_node = Node.build_question(
                new_question, iterator.value, new_team)

            self.__tree.insert(new_question_node, parent, direction)

    def end_game(self):
        answer = self.__view.yes_or_no_question(
            'Jogo finalizado! Deseja recomeçar? (s/n)\n')
        if answer == Answer.YES.value:
            self.play_game()
        elif answer == Answer.NO.value:
            self.__dump()
            exit(0)

    def run(self):
        switcher = {
            0: self.end_game,
            1: self.play_game,
        }
        while True:
            switcher[self.__view.show_options()]()
