class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)

        l = 0
        s2_map = {}

        for r in range(len(s2)):
            s2_map[s2[r]] = 1 + s2_map.get(s2[r], 0 )

            if r - l + 1 > len(s1):
                if s2_map[s2[l]] == 1:
                    s2_map.pop(s2[l])
                else:
                    s2_map[s2[l]] -= 1
                l += 1
            

            if s1_map == s2_map:
                return True

        return False


# TC: O(26*n)
# SC: O(n)