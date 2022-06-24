def sumSubarray(n, k):
    res = []
    sub_sum = 0
    for i in range(k):
        sub_sum += n[i]
    res.append(sub_sum)

    for j in range(1, len(n) - k + 1):
        sub_sum += n[j + k - 1]
        sub_sum -= n[j - 1]
        res.append(sub_sum)
    
    return res

print(sumSubarray([1,2,3,4,5,6], 3))