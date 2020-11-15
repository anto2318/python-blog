from collections import deque
from queue import Queue as Que

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):
        if self.queue:
            return self.queue[0]
        return "Queue is empty"

class Queue2:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return "Queue is empty"

    def peek(self):
        if self.queue:
            return self.queue[0]
        return "Queue is empty"

class Queue3:
    def __init__(self):
        self.queue = Que()
    
    def enqueue(self, data):
        self.queue.put(data)

    def dequeue(self):
        if self.queue.empty() == False:
            return self.queue.get()
        else:
            return "Queue is empty"

print("Queue")
queue = Queue()
queue.enqueue(101)
queue.enqueue(102)
print(queue.peek())
print(queue.dequeue())

print("------------")

print("Queue2")
queue2 = Queue2()
queue2.enqueue(101)
queue2.enqueue(102)
print(queue2.peek())
print(queue2.dequeue())

print("------------")

print("Queue3")
queue3 = Queue3()
queue3.enqueue(101)
queue3.enqueue(102)
print(queue3.dequeue())
print(queue3.dequeue())
print(queue3.dequeue())