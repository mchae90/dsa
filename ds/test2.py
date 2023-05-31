
def maxSubArray(nums):
    cur = nums[0]
    max_sum = nums[0]

    for i in nums:
        if i > cur:
            if cur < 0:
                i = cur
            else:
                cur += i

        else:
            cur += 1

        max_sum = max(cur, max_sum)
        print(cur, max_sum)

    return max_sum

print(maxSubArray([1,2]))     


# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# [1, 2]