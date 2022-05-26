def isPalindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        
        if s(l).lower() != s(r).lower():
            return False
        l += 1
        r -= 1
        
    return True


def alphaNum(c):
    None

# Key: Use left and right pointers, checking if the value at index is alphanumeric, inc/dec pointer indexes accordingly
# TC: O(n)
# SC: O(1) (only uses pointers, no extra memory needed)