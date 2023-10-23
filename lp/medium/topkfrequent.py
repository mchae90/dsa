
# Sorting
# TC: O(nlog(n))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count, key = lambda x:count[x], reverse = True)

        return count[:k]

# Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for key, v in count.items():
            heap.append((-v, key))

        heapq.heapify(heap)
        res = []

        for _ in range(k):
            _, ans = heapq.heappop(heap)
            res.append(ans)

        return res

# Bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  

        # len(nums) + 1 since 0-indexed
        freq = [[]] * (len(nums) + 1)

        for key, v in count.items():
            freq[v].append(key)

        res = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
# Bucket sort            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        freq = [[] for i in range(len(nums) + 1)]

        for num, count in counter.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                k -= 1

                if k == 0:
                    return res
