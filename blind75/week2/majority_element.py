class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 0
        
        for i in nums:
            if i == ans:
                count += 1
            else:
                if count == 0:
                    ans = i
                    count += 1
                else:
                    count -= 1
                    
        return ans

# Can use a hash map but will be O(n) SC.  Use a counter and variable to keep track.  Majority element will always result in positive count at the end
# TC: O(n)
# SC: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cur = None

        for n in nums:
            if cur == n:
                count += 1
            else:
                if count == 0:
                    cur = n
                    count += 1
                else:
                    count -= 1

        return cur
