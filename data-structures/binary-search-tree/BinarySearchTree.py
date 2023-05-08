from Node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        self.__root = None

    def is_empty(self) -> bool:
        return self.__root == None

    def __insert(self, value, root):
        if self.is_empty():
            self.__root = Node(value)
            return

        if root == None:
            return Node(value)

        if value < root.value:
            root.left = self.__insert(value, root.left)
        else:
            root.right = self.__insert(value, root.right)
        return root

    def __min(self, root):
        while root.left:
            root = root.left

        return root

    def __remove(self, key, root):
        if root == None:
            return root

        if key < root.value:
            root.left = self.__remove(key, root.left)
            return root
        elif key > root.value:
            root.right = self.__remove(key, root.right)
            return root
        else:
            if root.left and root.right:
                new_root = self.__min(root.right)
                root.value = new_root.value
                root.right = self.__remove(new_root.value, root.right)
                return root
            else:
                if root.left:
                    return root.left
                elif root.right:
                    return root.right
                else:
                    return None

    def __pre_order(self, root):
        if root != None:
            print(root.value, end=' ')
            self.__pre_order(root.left)
            self.__pre_order(root.right)

    def __post_order(self, root):
        if root != None:
            self.__post_order(root.left)
            self.__post_order(root.right)
            print(root.value, end=' ')

    def __in_order(self, root):
        if root != None:
            self.__in_order(root.left)
            print(root.value, end=' ')
            self.__in_order(root.right)

    def search(self, key):
        root = self.__root

        while root != None and root.value != key:
            if key < root.value:
                root = root.left
            else:
                root = root.right

        if root == None:
            raise Exception('The given element does not exist in the tree')

        return root.value

    def insert(self, value):
        self.__insert(value, self.__root)

    def remove(self, key):
        self.__remove(key, self.__root)

    def print_pre_order(self):
        self.__pre_order(self.__root)

    def print_post_order(self):
        self.__post_order(self.__root)

    def print_in_order(self):
        self.__in_order(self.__root)
