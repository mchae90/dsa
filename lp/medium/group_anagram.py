class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            hmap = [0] * 26

            for c in s:
                hmap[ord(c) - ord('a')] += 1
            
            res[tuple(hmap)].append(s)

        return res.values()

# TC: O(m*n)
# SC: O(m) (worst case)