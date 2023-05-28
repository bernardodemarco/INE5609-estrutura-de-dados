from models.QuestionNode import QuestionNode
from models.AnswerNode import AnswerNode


class DecisionTree:
    def __init__(self, initial_team) -> None:
        self.__root = AnswerNode(initial_team)

    @property
    def root(self):
        return self.__root

    def insert(self, new_node, node=None, direction=None):
        if node is None and direction is None:
            self.__root = new_node
            return

        if direction == 'correct_answer':
            node.correct_answer = new_node
        elif direction == 'wrong_answer':
            node.wrong_answer = new_node

    def __pre_order(self, root):
        if root is not None:
            print(root.value)
            if isinstance(root, QuestionNode):
                self.__pre_order(root.correct_answer)
                self.__pre_order(root.wrong_answer)

    def print_pre_order(self):
        self.__pre_order(self.__root)
