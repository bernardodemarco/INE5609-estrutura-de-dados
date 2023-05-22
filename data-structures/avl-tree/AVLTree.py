from Node import Node


class AVLTree:
    def __init__(self) -> None:
        self.__root = None

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

        root.height = max(root.left.height, root.right.height) + 1
        new_root.height = max(new_root.left.height, new_root.right.height) + 1

        return new_root

    def __right_rotate(self, root: Node) -> Node:
        new_root = root.left
        right_subtree = new_root.right

        root.left = right_subtree
        new_root.right = root

        root.height = max(root.left.height, root.right.height) + 1
        new_root.height = max(new_root.left.height, new_root.right.height) + 1

        return new_root

    def __right_left_rotate(self, root: Node) -> Node:
        root.right = self.__right_rotate(root.right)
        return self.__left_rotate(root)

    def __left_right_rotate(self, root: Node) -> Node:
        root.left = self.__left_rotate(root.left)
        return self.__right_rotate(root)

    def __insert(self):
        pass

    def __remove(self):
        pass
