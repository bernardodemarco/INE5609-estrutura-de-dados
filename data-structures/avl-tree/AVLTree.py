from Node import Node


class AVLTree:
    def __init__(self) -> None:
        self.__root = None

    def __is_empty(self) -> bool:
        return self.__root is None

    def __get_height(self, root) -> int:
        if root is None:
            return 0

        return root.height

    def __get_balance_factor(self, root) -> int:
        if root is None:
            return 0

        return self.__get_height(root.left) - self.__get_height(root.right)

    def __left_rotate(self, root: Node) -> Node:
        new_root = root.right
        left_subtree = new_root.left

        root.right = left_subtree
        new_root.left = root

        root.height = max(self.__get_height(root.left),
                          self.__get_height(root.right)) + 1

        new_root.height = max(self.__get_height(
            new_root.left), self.__get_height(new_root.right)) + 1

        return new_root

    def __right_rotate(self, root: Node) -> Node:
        new_root = root.left
        right_subtree = new_root.right

        root.left = right_subtree
        new_root.right = root

        root.height = max(self.__get_height(root.left),
                          self.__get_height(root.right)) + 1

        new_root.height = max(self.__get_height(
            new_root.left), self.__get_height(new_root.right)) + 1

        return new_root

    def __right_left_rotate(self, root: Node) -> Node:
        root.right = self.__right_rotate(root.right)
        return self.__left_rotate(root)

    def __left_right_rotate(self, root: Node) -> Node:
        root.left = self.__left_rotate(root.left)
        return self.__right_rotate(root)

    def __insert(self, value, root):
        if root is None or self.__is_empty():
            return Node(value)

        if value < root.value:
            root.left = self.__insert(value, root.left)
        else:
            root.right = self.__insert(value, root.right)

        root.height = max(self.__get_height(root.left),
                          self.__get_height(root.right)) + 1

        balance_factor = self.__get_balance_factor(root)
        if balance_factor < -1:
            if value < root.right.value:
                return self.__right_left_rotate(root)

            return self.__left_rotate(root)
        elif balance_factor > 1:
            if value > root.left.value:
                return self.__left_right_rotate(root)

            return self.__right_rotate(root)

        return root

    def __min(self, root: Node) -> Node:
        iterator = root
        while iterator.left is not None:
            iterator = iterator.left

        return iterator

    def __remove(self, value, root):
        if root is None:
            return root

        if value < root.value:
            root.left = self.__remove(value, root.left)
        elif value > root.value:
            root.right = self.__remove(value, root.right)
        else:
            if root.left is not None and root.right is not None:
                successor = self.__min(root.right)
                root.value = successor.value
                root.right = self.__remove(successor.value, root.right)
            elif root.left is not None:
                return root.left
            elif root.right is not None:
                return root.right
            else:
                return None

        root.height = max(self.__get_height(root.left),
                          self.__get_height(root.right)) + 1

        balance_factor = self.__get_balance_factor(root)
        if balance_factor < -1:
            if self.__get_balance_factor(root.right) > 0:
                return self.__right_left_rotate(root)

            return self.__left_rotate(root)
        elif balance_factor > 1:
            if self.__get_balance_factor(root.left) < 0:
                return self.__left_right_rotate(root)

            return self.__right_rotate(root)

        return root

    def __pre_order(self, root) -> None:
        if root is not None:
            print(root.value, end=', ')
            self.__pre_order(root.left)
            self.__pre_order(root.right)

    def insert(self, value) -> None:
        self.__root = self.__insert(value, self.__root)

    def remove(self, value) -> None:
        self.__root = self.__remove(value, self.__root)

    def print_pre_order(self) -> None:
        self.__pre_order(self.__root)
