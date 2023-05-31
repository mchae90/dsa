from jmespath import search


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        l, r = 0, len(letters) - 1
        
        while l <= r:
            m = (l + r) //2
            
            if target >= letters[m]:
                l = m + 1
            
            elif target < letters[m]:
                r = m - 1
        
        return letters[l]

# Modified binary search
# TC: O(logn)