# while loop
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        i = len(s) - 1

        while i >= 0:
            if s[i] == " ":
                if res > 0:
                    break
            else:
                res += 1
            i -= 1

        
        return res
    
# for loop
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1, -1, -1):
            if res > 0 and s[i] == " ":
                break
            if s[i] != " ":
                res += 1
        
        return res