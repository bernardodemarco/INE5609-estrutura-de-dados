class Node:
    def __init__(self, value: str) -> None:
        self.__value = value
        self.__yes = None
        self.__no = None

    @staticmethod
    def build_question(question: str, correct_answer: str, wrong_answer: str):
        new_node = Node(question)
        new_node.yes = Node(correct_answer)
        new_node.no = Node(wrong_answer)
        return new_node

    def is_leaf(self) -> bool:
        return self.__yes is None and self.__no is None

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, new_value: str) -> None:
        self.__value = new_value

    @property
    def yes(self):
        return self.__yes

    @yes.setter
    def yes(self, new_yes):
        self.__yes = new_yes

    @property
    def no(self):
        return self.__no

    @no.setter
    def no(self, new_no):
        self.__no = new_no
