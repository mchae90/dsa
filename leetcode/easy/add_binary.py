#LC 67

def add_binary(a, b):
    carry = 0
    res = ''
    
    a, b = a[::-1], b[::-1]


    for i in range(max(len(a), len(b))):

        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0

        total = digit_a + digit_b + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2

    if carry:
        res = "1" + res

    return res


print(add_binary)