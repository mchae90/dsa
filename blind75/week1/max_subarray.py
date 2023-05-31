# n^3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur_sum = 0
                for k in range(i, j + 1):
                    cur_sum += nums[k]
                
                res = max(res, cur_sum)

        return res
    
# n^2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                res = max(res, cur_sum)

        return res

# Kadane's 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cur = 0

        for n in nums:
            cur = max(n, cur + n)
            res = max(cur, res)
        return res

def maxSubArray(nums):
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sum = max(cur_sum, max_sum)
        print(cur_sum, max_sum)

    return max_sum



maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
