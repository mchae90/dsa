def plus_one(digits):
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    
    i = len(digits) - 1
    carry_one = True

    while carry_one:
        if i > -1:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry_one = 0
        else:
            digits.insert(0,1)
            carry_one = 0
        i -= 1


    return digits

print(plus_one([9,7,8,9,9]))