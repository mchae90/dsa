class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for p in points:
            d = (p[0] ** 2) + (p[1] ** 2)
            min_heap.append((d, p))
        
        heapq.heapify(min_heap)

        res = []

        while k > 0:
            v = heapq.heappop(min_heap)
            res.append(v[1])
            k -= 1
        
        return res