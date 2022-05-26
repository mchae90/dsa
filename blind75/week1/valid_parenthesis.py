def isValid(s):
    hash_map = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []
    for i in s:
        if i in hash_map:
            if stack and stack[-1] == hash_map[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False

isValid('[]')

# Note: Use a stack only appending open parenthesis.  Check if character is open/closed using a hash map.
# TC: O(n) - worst case you go through entire array
# SC: O(n) - stack can be up to size of input