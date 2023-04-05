from LinkedQueue import LinkedQueue

queue = LinkedQueue(4)

queue.enqueue(10)
queue.enqueue(12)
queue.enqueue(14)
queue.enqueue(16)
# queue.enqueue(20)  # throws exception queue is full

print(queue)
print(f'HEAD VALUE {queue.head_element().value}')
print(f'HEAD NEXT VALUE {queue.head_element().next.value}\n')

print(f'REMOVED VALUE {queue.dequeue()}')
print(f'HEAD VALUE {queue.head_element().value}')
print(f'HEAD NEXT VALUE {queue.head_element().next.value} \n')
print(queue)

queue.enqueue(10)
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
# queue.dequeue()  # throws exception queue is empty

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(5)
print(queue)
