def binary_search(arr, t):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] < t:
            l = mid + 1
        elif arr[mid] > t:
            r = mid - 1
        else:
            return mid
    
    return -1

print(binary_search([], 3))