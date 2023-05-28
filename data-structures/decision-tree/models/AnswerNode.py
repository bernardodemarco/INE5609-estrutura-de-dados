from models.Node import Node


class AnswerNode(Node):
    def __init__(self, value: str) -> None:
        super().__init__(value)
