import heapq

def kClosest(points, k):
    
    min_heap = []

    for x, y in points:
        d = (x ** 2) + (y ** 2)
        min_heap.append([d, x, y])
        
    heapq.heapify(min_heap)
    
    print(min_heap)
    
    res = []
    
    for i in range(k):
        e = heapq.heappop((min_heap))
        res.append(e[1:])
        
    return res

print(kClosest([[3,3],[5,-1],[-2,4]], 2))