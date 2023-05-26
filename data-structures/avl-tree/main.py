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

tree.remove(95)
print('\n\nPRE-ORDER SEQUENCE AFTER DELETION OF 95 WITH LEFT-RIGHT ROTATE')
tree.print_pre_order()

tree.remove(31)
tree.remove(32)
tree.remove(29)
print('\n\nPRE-ORDER SEQUENCE AFTER DELETION OF 31, 32 AND 29 WITH RIGHT-LEFT ROTATE')
tree.print_pre_order()

tree.remove(55)
tree.remove(91)
tree.remove(85)
print('\n\nPRE-ORDER SEQUENCE AFTER DELETION OF 55, 91, AND 85 WITH RIGHT ROTATE')
tree.print_pre_order()
