def climbStairs(n):
    
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(5))