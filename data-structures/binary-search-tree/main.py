from BinarySearchTree import BinarySearchTree


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(10)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(11)
bst.insert(1)
bst.insert(6)
bst.insert(8)
bst.insert(14)


print('PRE-ORDER:')
bst.print_pre_order()
print('\nPOST-ORDER:')
bst.print_post_order()
print('\nIN-ORDER:')
bst.print_in_order()

bst.remove(14)
bst.remove(2)
bst.remove(7)
bst.remove(9)

print('')
print('\nREMOVED 14, 2 AND 7')
print('PRE-ORDER:')
bst.print_pre_order()
print('\nPOST-ORDER:')
bst.print_post_order()
print('\nIN-ORDER:')
bst.print_in_order()

bst.remove(5)
print('')
print('\nREMOVED TREE ROOT')
print('PRE-ORDER:')
bst.print_pre_order()
print('\nPOST-ORDER:')
bst.print_post_order()
print('\nIN-ORDER:')
bst.print_in_order()

