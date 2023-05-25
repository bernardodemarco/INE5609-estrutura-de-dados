from AVLTree import AVLTree


tree = AVLTree()

nums_to_insert = [39, 29, 85, 31, 55, 91]

for num in nums_to_insert:
    tree.insert(num)

print('PRE-ORDER SEQUENCE')
tree.print_pre_order()

tree.insert(32)
print('\n\nPRE-ORDER SEQUENCE AFTER LEFT ROTATE')
tree.print_pre_order()

tree.insert(50)
tree.insert(45)
print('\n\nPRE-ORDER SEQUENCE AFTER RIGHT ROTATE')
tree.print_pre_order()

tree.insert(60)
print('\n\nPRE-ORDER SEQUENCE AFTER LEFT-RIGHT ROTATE')
tree.print_pre_order()

tree.insert(95)
print('\n\nPRE-ORDER SEQUENCE AFTER LEFT ROTATE')
tree.print_pre_order()

tree.insert(94)
print('\n\nPRE-ORDER SEQUENCE AFTER RIGHT-LEFT ROTATE')
tree.print_pre_order()

tree.remove(60)
print('\n\nPRE-ORDER SEQUENCE AFTER DELETION OF 60 WITH LEFT ROTATE')
tree.print_pre_order()

# tree.remove(95)
# print('\n\nPRE-ORDER SEQUENCE AFTER DELETION OF 60 WITH LEFT ROTATE')
# tree.print_pre_order()

# tree.remove(8)
# tree.remove(7)
# tree.remove(4)
# tree.remove(6)
# tree.remove(1)
# tree.remove(2)
# tree.remove(5)

# print('\n\nPRE-ORDER SEQUENCE AFTER DELETIONS')
# print('REMOVED 8, 7, 4, 6, 1, 2')
# tree.print_pre_order()
