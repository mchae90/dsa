import heapq


lamps = [[-20,-3],[-10,-1],[-5,14],[11,15]]
benches = [-17,-10,-4,4,12,16]

# BRUTE FORCE - TLE
# def numOfLights(lamps, benches):
#     lamps.sort(key = lambda x: x[0])
#     res = []

#     for b in benches:
#         count = 0
#         for s, e in lamps:
#             if s <= b <= e:
#                 count += 1
#         res.append(count)

#     return res

def numOfLights(lamps, benches):
    # 1 = start, 2 = bench, 3 = end
    q = []
    for start, end in lamps:
        q.append((start, 1))
        q.append((end, 3))

    for b in benches:
        q.append((b, 2))

    q.sort(key = lambda x: (x[0], x[1]))

    res = []

    lights = 0
    for time, type in q:
        if type == 1:
            # on
            lights += 1
        elif type == 2:
            res.append(lights)
        else:
            # off
            lights -= 1

    return res


print(numOfLights(lamps, benches))