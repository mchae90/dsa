#LC 67

# def add_binary(a, b):
#     carry = 0
#     res = ''
    
#     a, b = a[::-1], b[::-1]


#     for i in range(max(len(a), len(b))):

#         digit_a = int(a[i]) if i < len(a) else 0
#         digit_b = int(b[i]) if i < len(b) else 0

#         total = digit_a + digit_b + carry
#         char = str(total % 2)
#         res = char + res
#         carry = total // 2

#     if carry:
#         res = "1" + res

#     return res

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def add_binary(a, b):
    
    pa, pb = len(a) - 1, len(b) - 1
    carry = 0
    binary = ''

    while pa >= 0 or pb >= 0 or carry:
        int_a = int(a[pa]) if pa >= 0 else -1
        int_b = int(b[pb]) if pb >= 0 else -1

        cur = carry + int_a + int_b 

        if cur > 1:
            carry = True
        else:
            carry = False
        
        cur %= 2

        binary = binary + str(cur)

        pa -= 1
        pb -= 1
        # print(binary)
    
    return binary


print(add_binary("1010", "1011"))