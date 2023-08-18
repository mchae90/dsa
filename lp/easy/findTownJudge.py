class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)

        for p1, p2 in trust:
            count[p1] -= 1
            count[p2] += 1
        
        for i in range(1, len(count)):
            if count[i] == n - 1:
                return i
        
        return -1