class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            prod = 1

            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            
            res.append(prod)

        return res
    
# TC: O(n^2)