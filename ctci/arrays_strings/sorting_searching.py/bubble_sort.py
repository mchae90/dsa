def bubbleSort(nums):

    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

print(bubbleSort([3,9,1,3]))

def bubbleSort2(nums):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
    return nums

print(bubbleSort2([3,9,1,3]))