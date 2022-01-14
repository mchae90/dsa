# LC 69
# def sqrt(x):
#     i = 1

#     while i * i <= x:
#         i += 1
    
#     return i - 1

def sqrt(x):
    left = 1
    right = x

    if (x == 0 or x == 1) :
        return x

    while left <= right:
        mid = (right + left) // 2

        if mid * mid == x:
            return mid

        if mid * mid < x:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer            


print(sqrt(45))