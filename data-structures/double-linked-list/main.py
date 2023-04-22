from DoubleLinkedList import DoubleLinkedList


def print_list_data(list_pointer: DoubleLinkedList) -> None:
    try:
        print(
            f'CURSOR = {list_pointer.get_current()} - START = {list_pointer.get_start()} - END = {list_pointer.get_end()} - LENGTH = {list_pointer.get_length()}')
        list_pointer.print_list()
    except:
        list_pointer.print_list()


linked_list = DoubleLinkedList(10)

linked_list.insert_at_start(10)
linked_list.insert_at_end(15)
print_list_data(linked_list)

if linked_list.contains(10):
    linked_list.insert_after_current(10.1)

if linked_list.contains(5):
    linked_list.insert_before_current(4.9)

if linked_list.contains(15):
    linked_list.insert_before_current(14.9)
print_list_data(linked_list)

linked_list.insert_at_position(2, 10.05)
print_list_data(linked_list)

position = linked_list.get_position_of(14.9)
print('REMOVED ELEMENT =', linked_list.remove_at_position(position))
print('REMOVED ELEMENT =', linked_list.remove_at_position(1))
print('REMOVED ELEMENT =', linked_list.remove_at_position(linked_list.get_length()))
print_list_data(linked_list)

linked_list.insert_at_end(10.15)
linked_list.insert_at_position(1, 10)
print_list_data(linked_list)

print('POSITION OF 10.1 =', linked_list.get_position_of(10.1))
linked_list.insert_after_current(10.125)
linked_list.insert_at_end(10.2)
print_list_data(linked_list)

print('REMOVED ELEMENT =', linked_list.remove_element(10.05))
print('REMOVED ELEMENT =', linked_list.remove_at_position(3))
print('REMOVED ELEMENT =', linked_list.remove_first())
print('REMOVED ELEMENT =', linked_list.remove_last())
print_list_data(linked_list)

try:
    print('REMOVED ELEMENT =', linked_list.remove_element(10.2))
except Exception as err:
    print(err)
    print_list_data(linked_list)

try:
    print('REMOVED ELEMENT =', linked_list.remove_at_position(3))
except Exception as err:
    print(err)
    print_list_data(linked_list)

print(linked_list.contains(10))
print(linked_list.contains(10.1))
print(linked_list.contains(10.05))
print(linked_list.contains(10.15))
