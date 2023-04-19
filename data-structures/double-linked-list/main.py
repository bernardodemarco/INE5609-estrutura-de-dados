from DoubleLinkedList import DoubleLinkedList


def print_list_data(list_pointer: DoubleLinkedList) -> None:
    """
    Summary line.

    Args:
        arg1 (type): description.

    Returns:
        type: description.

    Raises:
        Exception: when.

    """
    try:
        print(
            f'START = {list_pointer.get_start()} - END = {list_pointer.get_end()} - LENGTH = {list_pointer.get_length()}')
        list_pointer.print_list()
    except:
        list_pointer.print_list()


linked_list = DoubleLinkedList(10)

linked_list.remove_last()

# linked_list.insert_at_start(10)
# linked_list.insert_at_end(15)
# if linked_list.contains(5):
#     linked_list.insert_before_current(4.9)
# print_list_data(linked_list)

# if linked_list.contains(10):
#     linked_list.insert_after_current(10.1)

# if linked_list.contains(15):
#     linked_list.insert_before_current(14.9)
# print_list_data(linked_list)

# linked_list.insert(2, 10.05)
# print_list_data(linked_list)

# position = linked_list.get_position_of(14.9)
# linked_list.remove_at_position(position)
# linked_list.remove_first()
# linked_list.remove_last()
# print('CURRENT ELEMENT =', linked_list.get_current())
# print_list_data(linked_list)

# linked_list.insert(3, 10.15)
# linked_list.insert(1, 10)
# print_list_data(linked_list)

# linked_list.remove_element(10.05)
# linked_list.remove_at_position(3)
# print_list_data(linked_list)

# print(linked_list.contains(10))
# print(linked_list.contains(10.1))
# print(linked_list.contains(10.05))
# print(linked_list.contains(10.15))
