class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min_stack:
            min_val = min(val, self.min_stack[-1])
            self.min_stack.append(min_val)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Key: Create another stack and keep track of each min of each index up to that point.
# You are sacrificing space for better time.  
# TC: O(1)