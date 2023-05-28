from models.AnswerNode import AnswerNode
from models.Node import Node


class QuestionNode(Node):
    def __init__(self, value: str) -> None:
        super().__init__(value)
        self.__correct_answer = None
        self.__wrong_answer = None

    @property
    def correct_answer(self) -> AnswerNode:
        return self.__correct_answer

    @correct_answer.setter
    def correct_answer(self, new_answer: AnswerNode):
        self.__correct_answer = new_answer

    @property
    def wrong_answer(self) -> AnswerNode:
        return self.__wrong_answer

    @wrong_answer.setter
    def wrong_answer(self, new_answer: AnswerNode):
        self.__wrong_answer = new_answer
