from Node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        self.__root = None

    def is_empty(self) -> bool:
        return self.__root is None

    def __insert(self, value, root):
        if self.is_empty():
            self.__root = Node(value)
            return

        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.__insert(value, root.left)
        else:
            root.right = self.__insert(value, root.right)
        return root

    def __min(self, root):
        iterator = root
        while iterator.left is not None:
            iterator = iterator.left

        return iterator

    def __remove(self, key, root):
        if root is None:
            return root

        if key < root.value:
            root.left = self.__remove(key, root.left)
            return root
        elif key > root.value:
            root.right = self.__remove(key, root.right)
            return root
        else:
            if root.left is not None and root.right is not None:
                successor = self.__min(root.right)
                root.value = successor.value
                root.right = self.__remove(successor.value, root.right)
                return root
            else:
                if root.left is not None:
                    return root.left
                elif root.right is not None:
                    return root.right
                else:
                    return None

    def __pre_order(self, root, values):
        if root is not None:
            values.append(root)
            self.__pre_order(root.left, values)
            self.__pre_order(root.right, values)

        return values

    def __post_order(self, root, values):
        if root is not None:
            self.__post_order(root.left, values)
            self.__post_order(root.right, values)
            values.append(root)

        return values

    def __in_order(self, root, values):
        if root is not None:
            self.__in_order(root.left, values)
            values.append(root)
            self.__in_order(root.right, values)

        return values

    def __balance(self, arr, lower, upper):
        middle_element_index = (upper - lower) // 2 + lower
        if upper >= lower:
            self.__insert(arr[middle_element_index].value, self.__root)
            self.__balance(arr, lower, middle_element_index - 1)
            self.__balance(arr, middle_element_index + 1, upper)

    def insert(self, value):
        self.__insert(value, self.__root)

    def remove(self, key):
        self.__remove(key, self.__root)

    def print_pre_order(self):
        pre_order_sequence = self.__pre_order(self.__root, [])

        for i in range(len(pre_order_sequence) - 1):
            print(pre_order_sequence[i].value, end=', ')

        print(pre_order_sequence[-1].value)

    def print_post_order(self):
        post_order_sequence = self.__post_order(self.__root, [])

        for i in range(len(post_order_sequence) - 1):
            print(post_order_sequence[i].value, end=', ')

        print(post_order_sequence[-1].value)

    def print_in_order(self):
        in_order_sequence = self.__in_order(self.__root, [])

        for i in range(len(in_order_sequence) - 1):
            print(in_order_sequence[i].value, end=', ')

        print(in_order_sequence[-1].value)

    def search(self, key):
        iterator = self.__root

        while iterator is not None and iterator.value != key:
            if key < iterator.value:
                iterator = iterator.left
            else:
                iterator = iterator.right

        if iterator is None:
            raise Exception('The given element does not exist in the tree')

        return iterator.value

    def balance_tree(self):
        in_order_sequence = self.__in_order(self.__root, [])
        self.__root = None
        self.__balance(in_order_sequence, 0, len(in_order_sequence) - 1)
