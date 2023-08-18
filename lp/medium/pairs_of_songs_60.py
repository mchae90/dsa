class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0

        hmap = defaultdict(int)

        for t in time:
            # if multiple of 60, add to pairs all combinations of hmap[0]
            if t % 60 == 0:
                pairs += hmap[0]
            # if not multiple of 60, add to pairs all combinations of hmap[60 - (t % 60)]
            else:
                pairs += hmap[60 - (t % 60)]
            
            hmap[t % 60] += 1
        
        return pairs
    
# TC: O(n)
# SC: O(1)