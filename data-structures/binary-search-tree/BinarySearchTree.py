from Node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        self.__root = None

    def __insert(self, value, root):
        if self.__root == None:
            self.__root = Node(value)
            return

        if root == None:
            return Node(value)
        elif value < root.value:
            root.left = self.__insert(value, root.left)
            return root
        else:
            root.right = self.__insert(value, root.right)
            return root

    def __pre_order(self, root):
        if root == None:
            return None

        print(root.value, end=' ')
        self.__pre_order(root.left)
        self.__pre_order(root.right)

    def __post_order(self, root):
        if root == None:
            return None

        self.__post_order(root.left)
        self.__post_order(root.right)
        print(root.value, end=' ')

    def __in_order(self, root):
        if root == None:
            return None

        self.__in_order(root.left)
        print(root.value, end=' ')
        self.__in_order(root.right)

    def insert(self, value):
        self.__insert(value, self.__root)

    def print_pre_order(self):
        self.__pre_order(self.__root)

    def print_post_order(self):
        self.__pre_order(self.__root)

    def print_in_order(self):
        self.__pre_order(self.__root)
