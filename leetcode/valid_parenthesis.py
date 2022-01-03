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