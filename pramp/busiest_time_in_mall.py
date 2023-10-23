def find_busiest_period(data):
    n = len(data)
    peak_time = 0

    cur_traffic = 0
    max_traffic = 0

    for i in range(len(data)):
        d = data[i]
        time, count, status = d[0], d[1], d[2]

        if status == 0:
            count *= -1
        
        cur_traffic += count
        
        if i < n - 1 and data[i + 1][0] != data[i][0]:
            continue

        if cur_traffic > max_traffic:
            max_traffic = cur_traffic
            peak_time = time
    
    return peak_time
  
    # hmap = {}

    # for d in data:
    #     time, count, status = d[0], d[1], d[2]
    #     change_in_visitors = count

    #     if status == 0:
    #         change_in_visitors = count * -1

    #     if time not in hmap:
    #         hmap[time] = change_in_visitors
    #     else:
    #         hmap[time] += change_in_visitors
        
    # print(hmap)

    # answer = ''
    # max_traffic = 0
    # for k, v in hmap.items():
    #     if v > max_traffic:
    #         max_traffic = v
    #         answer = k

    # return answer
  

# [[1487799425,14,1], 14
#  [1487799425,4,0], 10
#  [1487799425,2,0], 8

#  [1487800378,10,1], 18

#  [1487801478,18,0], 0
#  [1487801478,18,1], 18

#  [1487901013,1,0], 17

#  [1487901211,7,1], 24 
#  [1487901211,7,0]] 17 x

print(find_busiest_period(
[[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,18,1],[1487901013,1,0],[1487901211,7,1],[1487901211,7,0]]
))