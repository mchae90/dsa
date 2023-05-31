class NumArray:

    def __init__(self, nums):
        self.nums = nums
        count = 0
        
        for i, v in enumerate(nums):
            count += v
            self.nums[i] = count

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left - 1]

n = NumArray([-2, 0, 3, -5, 2, -1])
print(n.getNums())


# Count sum up to each index in init.  Sum of range will be s[r] - s[l - 1]
# TC: O(n)
# SC: O(n)