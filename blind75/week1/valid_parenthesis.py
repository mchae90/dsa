class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        
        par_stack = []
        
        for c in s:
            if c in par_map:
                if par_stack and par_stack[-1] == par_map[c]:
                    par_stack.pop()
                else:
                    return False
            else:
                par_stack.append(c)
                
        if par_stack:
            return False
    
        return True

# Note: Use a stack only appending open parenthesis.  Check if character is open/closed using a hash map.
# TC: O(n) - worst case you go through entire array
# SC: O(n) - stack can be up to size of input