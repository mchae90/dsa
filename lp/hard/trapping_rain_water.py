# TC: O(n), SC: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        left_max = [0] * len(height)

        for i in range(len(left_max)):
            left = max(left, height[i])
            left_max[i] = left

        right = 0
        right_max = [0] * len(height)

        for i in range(len(right_max) - 1, -1, -1):
            right = max(right, height[i])
            right_max[i] = right

        print(left_max, right_max)

        res = 0

        for i in range(len(left_max)):
            amount = min(left_max[i], right_max[i]) - height[i]

            if amount > 0:
                res += amount

        return res
    
# TC: O(n), SC: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]

        return res