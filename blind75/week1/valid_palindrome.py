class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

# Key: Use left and right pointers, checking if the value at index is alphanumeric, inc/dec pointer indexes accordingly
# TC: O(n)
# SC: O(1) (only uses pointers, no extra memory needed)