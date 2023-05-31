class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            for i in range(len(nums)):
                nums[i], nums[-1] = nums[-1], nums[i]
        
        return nums

# TC: O(n * k)
# SC: O(1)
# TLE

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = nums.copy()

        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = copy[i]
        
        return nums

# TC: O(n)
# SC: O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        k = k % len(nums)
        
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

# TC: O(n)
# SC: O(1)