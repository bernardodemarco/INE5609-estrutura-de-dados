from Node import Node
from enums import Direction


class DecisionTree:
    def __init__(self, initial_team) -> None:
        self.__root = Node(initial_team)

    @property
    def root(self):
        return self.__root

    def insert(self, new_node, parent, direction):
        if direction is None:
            self.__root = new_node
            return

        if direction is Direction.CORRECT_ANSWER:
            parent.yes = new_node
        elif direction is Direction.WRONG_ANSWER:
            parent.no = new_node

    def __pre_order(self, root):
        if root is not None:
            print(root.value)
            self.__pre_order(root.yes)
            self.__pre_order(root.no)

    def print_pre_order(self):
        self.__pre_order(self.__root)
