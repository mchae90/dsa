# LC 35
def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            l = mid + 1
        else:
            l = mid - 1
    
    return l

print(searchInsert([2], 1))
