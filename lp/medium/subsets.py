class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i):
            if i == len(nums):
                res.append(subsets.copy())
                return
            
            # decision to append nums[i]
            subsets.append(nums[i])
            dfs(i + 1)

            # decision to not to append nums[i]
            subsets.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

# TC: 2^n