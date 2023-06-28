# Recursive
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

# Memoization
class Solution:
    def fib(self, n: int) -> int:
        cache = {0: 0, 1: 1}

        if n in cache:
            return cache[n]
        cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return cache[n]

# Iterative
class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1

        for _ in range(n):
            temp = a + b
            a = b
            b = temp
        
        return a