class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def peek(self):
        return self.stack[len(self.stack) -1]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()


class MyQueue:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def enque(self, item):
        self.stack_push.append(item)
    
    def deque(self):
        if len(self.stack_pop) == 0:
            if len(self.stack_push) == 0: 
                print('MyQueue empty')
                return None
            while len(self.stack_push) > 0:
                self.stack_pop.append(self.stack_push.pop())
            return self.stack_pop.pop()
        else:
            return self.stack_pop.pop()

# q = MyQueue()
# q.enque(1)
# q.enque(2)
# q.enque(3)
# # print(q.deque())
# print(q.deque())
# print(q.deque())
# print(q.deque())


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return None
        else:
            self.stack.pop()

    def isEmpty(self):
        return not self.stack

    def getSize(self):
        return len(self.stack)

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[len(self.stack) - 1]

s = MyStack()
print(s.isEmpty())
# print(s.push(1))
print(s.getSize())
print(s.peek())