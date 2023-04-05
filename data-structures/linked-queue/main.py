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

queue = LinkedQueue(4)

queue.enqueue(node_1)
queue.enqueue(node_2)
queue.enqueue(node_3)
queue.enqueue(node_4)
# queue.enqueue(node_5) throws exception queue is full

print(queue)
print(f'HEAD VALUE {queue.head_element().value}')
print(f'HEAD NEXT VALUE {queue.head_element().next.value}\n')

print(f'REMOVED VALUE {queue.dequeue().value}')
print(f'HEAD VALUE {queue.head_element().value}')
print(f'HEAD NEXT VALUE {queue.head_element().next.value} \n')
print(queue)

queue.enqueue(node_1)
print(queue)
print(f'HEAD VALUE {queue.head_element().value}')
print(f'HEAD NEXT VALUE {queue.head_element().next.value}\n')

queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue)
print(f'HEAD VALUE {queue.head_element().value}')
print(f'HEAD NEXT VALUE {queue.head_element().next}\n')

queue.dequeue()
print(queue, '\n')
# queue.dequeue() throws exception queue is empty

queue.enqueue(node_5)
queue.enqueue(node_6)
queue.enqueue(node_7)
queue.enqueue(node_8)
print(queue)
