from BinarySearchTree import BinarySearchTree


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(10)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(11)
print('PRE-ORDER:')
bst.print_pre_order()
print('\nPOST-ORDER:')
bst.print_post_order()
print('\nIN-ORDER:')
bst.print_in_order()
