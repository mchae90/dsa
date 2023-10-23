class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0 for _ in range(len(citations) + 1)]
        # for 5 citations:
        # index = 0,1,2,3,4,5
        # value = 0,0,0,0,0,0

        for count in citations:
            if count >= n:
                bucket[n] += 1
            else:
                bucket[count] += 1
        
        print(bucket)

        possible_hval = 0

        for i in range(len(bucket) - 1, -1, -1):
            possible_hval += bucket[i]
            if possible_hval >= i:
                return i

        return possible_hval