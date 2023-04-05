from LinkedList import LinkedList


linked_list = LinkedList()

print(f'LENGTH = {linked_list.length}')
print(f'EMPTY = {linked_list.is_empty()}\n')

linked_list.insert_at_end(16)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_at_start(6)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'{linked_list}\n')

linked_list.insert_at_start(8)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'{linked_list}\n')

linked_list.insert_at_start(10)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'{linked_list}\n')

linked_list.insert_at_end(20)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_at_end(40)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_after(40, 41)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_after(6, 6.1)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

try:
    linked_list.insert_after(2, 6.1)
except:
    print('error! target does not exist')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_before(10, 9)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')

linked_list.insert_before(16, 15.9)
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')


try:
    linked_list.insert_before(1, 1.5)
except:
    print('error! target does not exist')
print(f'LENGTH = {linked_list.length}')
print(f'START = {linked_list.get_first()}')
print(f'END = {linked_list.get_last()}')
print(f'{linked_list}\n')
