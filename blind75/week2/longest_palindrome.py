class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        
        ans = 0
        
        for n in counter.values():
            ans += (n // 2 * 2)
        
        if ans < len(s):
            ans += 1
        
        return ans

# TC: O(n)
# SC: O(1)