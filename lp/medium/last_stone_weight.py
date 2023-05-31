class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)

            if a != b:
                v = a - b
                heapq.heappush(stones, v)
        
        if not stones:
            return 0
        
        return stones[0] * -1