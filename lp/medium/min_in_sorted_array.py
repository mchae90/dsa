class Solution:
    def findMin(self, s: List[int]) -> int:
        l, r = 0, len(s) - 1

        while l < r:
            m = (l + r) // 2

            if s[m] > s[r]:
                l = m + 1
            else:
                r = m
        
        return s[l]