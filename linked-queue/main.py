from Node import Node
from LinkedQueue import LinkedQueue

node_1 = Node(18)
node_2 = Node(8)
node_3 = Node(10)
node_4 = Node(20)
node_5 = Node(11)
node_6 = Node(15)
node_7 = Node(19)
node_8 = Node(25)
node_9 = Node(50)

queue = LinkedQueue(4)

queue.enqueue(node_1)
queue.enqueue(node_3)
queue.enqueue(node_4)
queue.enqueue(node_6)

print(queue)

print('HEAD VALUE', queue.head_element().value)
print('HEAD NEXT VALUE', queue.head_element().next.value)
print('\n')

print('REMOVED VALUE', queue.dequeue().value)
print('HEAD VALUE', queue.head_element().value)
print('HEAD NEXT VALUE', queue.head_element().next.value)
print(queue)
print('\n')


print('REMOVED VALUE', queue.dequeue().value)
print('HEAD VALUE', queue.head_element().value)
print('HEAD NEXT VALUE', queue.head_element().next.value)
print(queue)
print('\n')

print('REMOVED VALUE', queue.dequeue().value)
print('HEAD VALUE', queue.head_element().value)
print('HEAD NEXT VALUE', queue.head_element().next)
print(queue)
print('\n')

print('REMOVED VALUE', queue.dequeue().value)
print(queue)
print('\n')

queue.enqueue(node_2)
queue.enqueue(node_5)
queue.enqueue(node_7)
queue.enqueue(node_8)
# queue.enqueue(node_9)
print(queue)
