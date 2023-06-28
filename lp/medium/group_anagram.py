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


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        res = []

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            if tuple(freq) in hmap:
                hmap[tuple(freq)].append(s)
            else:
                hmap[tuple(freq)] = [s]
        
        for v in hmap.values():
            res.append(v)
        
        return res