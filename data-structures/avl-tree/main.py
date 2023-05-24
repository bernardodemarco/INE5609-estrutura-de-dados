from AVLTree import AVLTree


tree = AVLTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.insert(4.5)
tree.insert(4.25)

print('PRE-ORDER SEQUENCE BEFORE DELETIONS')
tree.print_pre_order()

tree.remove(8)
tree.remove(7)
tree.remove(4)
tree.remove(6)
tree.remove(1)
tree.remove(2)
tree.remove(5)

print('\n\nPRE-ORDER SEQUENCE AFTER DELETIONS')
print('REMOVED 8, 7, 4, 6, 1, 2')
tree.print_pre_order()

# nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
# for num in nums:
#     tree.insert(num)

# tree.print_pre_order()

# tree.remove(10)
# print('')
# tree.print_pre_order()
