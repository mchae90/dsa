# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        while l < r:
            
            mid = (r + l) // 2
            
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        
        return l

# Key: when the midpoint is not bad, move left pointer to mid + 1.  
# This will cause loop to break
# TC: O(n)
# SC: O(1)