class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] not in hmap:
                hmap[s[r]] = 1
            else:
                hmap[s[r]] += 1
            # hmap[s[r]] = 1 + hmap.get(s[r], 0)
            
            if (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
    
# TC: O(n)
# SC: O(26n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hmap = {}

        for r in range(len(s)):
            if s[r] in hmap:
                hmap[s[r]] += 1
            else:
                hmap[s[r]] = 1
            
            if (r - l + 1) - max(hmap.values()) <= k:
                res = max(res, r - l + 1)
            else:
                hmap[s[l]] -= 1
                l += 1
        
        return res
                