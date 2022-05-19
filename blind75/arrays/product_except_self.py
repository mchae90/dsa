def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in nums:
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

    # [1,2,3,4]
    # [1,1,2,6] - l
    # [24,12,4,1] - r
    # [24,12,8,6]

# Note: Answer is every item to the left times every item to the right.  
# Create result array with all "1" values.  Loop left to right, multiplying everything to the left.  
# Loop again backwards, this time multiplying everything to the right.
# TC: O(n), SC: O(1) (problem states output array does not count as extra space)