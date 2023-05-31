class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        myset = set()

        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            res = max(res, r - l + 1)
        
        return res

# TC: O(n)
# SC: O(n)