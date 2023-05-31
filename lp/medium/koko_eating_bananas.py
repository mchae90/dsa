class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            k = (l + r) // 2
            total = 0

            for p in piles:
                t = math.ceil(p / k)
                total += t

            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res


# TC: log(n)
# SC: O(1)