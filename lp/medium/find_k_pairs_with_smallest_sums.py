class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        visited = set()
        res = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0,0))

        while len(res) < k and heap:
            pop = heapq.heappop(heap)
            res.append((nums1[pop[1]], nums2[pop[2]]))

            if pop[1] + 1 < len(nums1) and (pop[1] + 1, pop[2]) not in visited:
                heapq.heappush(heap, (nums1[pop[1] + 1] + nums2[pop[2]], pop[1] + 1, pop[2]))
                visited.add((pop[1] + 1, pop[2]))
            if pop[2] + 1 < len(nums2) and (pop[1], pop[2] + 1) not in visited:
                heapq.heappush(heap, (nums1[pop[1]] + nums2[pop[2] + 1], pop[1], pop[2] + 1))
                visited.add((pop[1], pop[2] + 1))
        
        return res