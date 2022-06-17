class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if self.stack2:
            return self.stack2.pop()
        else:
            return None
        

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        if self.stack1:
            return self.stack1[0]
        return None
        

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# [6,7]
# [5]