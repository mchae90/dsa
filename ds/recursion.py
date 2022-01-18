def get_factorial(n):
    if n < 0:
        return -1
    if n < 2:
        return 1
    else:
        return n * get_factorial(n - 1)

print(get_factorial(5))

def get_fib(n):
    if n < 0:
        print('incorrect input')
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return get_fib(n - 1) + get_fib(n - 2)

print(get_fib(6))