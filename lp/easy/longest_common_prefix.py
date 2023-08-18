class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l, r = 0, len(strs[0])

        for i in range(1, len(strs)):
            while r > 0 and strs[0][l:r] != strs[i][l:r]:
                r -= 1
        
        return strs[0][l:r]

# TC: O(n)
# SC: O(1)