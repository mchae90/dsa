# from collections import deque

# q = deque('hello')
# q.append(1)
# print(q)

# Queue with two stacks

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)
    
    def dequeue(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
            else:
                print('Queue is empty')
                return None
    

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
# print(q.deque())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue()) 