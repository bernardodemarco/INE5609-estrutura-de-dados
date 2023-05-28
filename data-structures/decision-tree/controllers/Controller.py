from views.Screen import Screen
from models.DecisionTree import DecisionTree
from models.AnswerNode import AnswerNode
from models.QuestionNode import QuestionNode


class Controller:
    def __init__(self) -> None:
        self.__screen = Screen()
        self.__tree = DecisionTree('Chapecoense')

    def start_game(self):
        answer = self.__screen.guess_answer(self.__tree.root.value)

        if answer == 's':
            return self.end_game()

        (new_team, new_question) = self.__screen.ask_difference(
            self.__tree.root.value)
        question_node = QuestionNode(new_question)
        question_node.correct_answer = self.__tree.root
        question_node.wrong_answer = AnswerNode(new_team)

        self.__tree.insert(question_node)
        self.__tree.print_pre_order()

    def resume_game(self):
        iterator = self.__tree.root
        direction = None
        while True:
            self.__screen.show_message(iterator.value + '(s/n)\n')
            answer = self.__screen.read_answer()
            if answer == 's':
                if isinstance(iterator.correct_answer, AnswerNode):
                    direction = 'correct_answer'
                    break
                iterator = iterator.correct_answer
            elif answer == 'n':
                if isinstance(iterator.wrong_answer, AnswerNode):
                    direction = 'wrong_answer'
                    break
                iterator = iterator.wrong_answer
        team_name = ''
        if direction == 'correct_answer':
            team_name = iterator.correct_answer.value
        else:
            team_name = iterator.wrong_answer.value

        answer = self.__screen.guess_answer(team_name)
        if answer == 's':
            self.end_game()
        elif answer == 'n':
            (new_team, new_question) = self.__screen.ask_difference(team_name)
            question_node = QuestionNode(new_question)
            question_node.correct_answer = AnswerNode(team_name)
            question_node.wrong_answer = AnswerNode(new_team)
            self.__tree.insert(question_node, iterator, direction)
            self.__tree.print_pre_order()

    def end_game(self):
        self.__screen.show_message(
            'Obrigado por jogar o Akinator, versão times de futebol!')
        exit(0)

    def run(self):
        switcher = {
            0: self.end_game,
            1: self.start_game,
            2: self.resume_game
        }
        while True:
            switcher[self.__screen.show_options()]()
