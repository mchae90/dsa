class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for c in s:
            if not stack:
                stack.append([c, 1])
            else:
                if stack[-1][0] == c:
                    if stack[-1][1] < k - 1:
                        stack[-1][1] += 1
                    else:
                        stack.pop()
                else:
                    stack.append([c, 1])

        res = ""
        while stack:
            pop = stack.pop()
            for i in range(pop[1]):
                res += pop[0]
        
        return res[::-1]