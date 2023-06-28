# Not using a set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # if value of left most index is zero, exit the loop.
            # nums is already sorted and if nums[i] > 0, any values to right will be 0
            if nums[i] > 0:
                break
            # if value of left most value is same as previous, continue to next iteration
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    #after appending, check for other l and r values that would negate nums[i]
                    l += 1
                    r -= 1 
                    # check for if any of nums[l] values are same as prev
                    # if so, move onto next iteration
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

# TC: O(nlog(n)) + O(n^2)
# SC: O(n) - python sort:

# Using a set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            if nums[i] > 0:
                break

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res