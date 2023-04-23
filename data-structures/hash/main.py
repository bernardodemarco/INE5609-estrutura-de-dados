from Hash import Hash

hash = Hash(6)

hash.insert(27)
hash.insert(2)
hash.insert(4)
hash.insert(11)
hash.insert(3)
hash.insert(18)
hash.insert(47)
hash.insert(29)
hash.insert(19)
hash.insert(39)
hash.insert(23)
hash.insert(13)

hash.print_hash()
retrieved = hash.get_item(39)
print('RETRIEVED ELEMENT =', retrieved)
retrieved = hash.get_item(139)
print('RETRIEVED ELEMENT =', retrieved)

try:
    print('REMOVED =', hash.remove(4))
    print('REMOVED =', hash.remove(47))
    print('REMOVED =', hash.remove(18))
    print('REMOVED =', hash.remove(100))
except Exception as err:
    print(err)
