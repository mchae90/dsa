class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_p = 0

        for i, v in enumerate(nums):
            if max_p < i:
                return False
            max_p = max(max_p, i + v)

        
        return True

# Greedy algorithm
# TC: O(n)
# SC: O(1)