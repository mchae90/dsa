# LC 53

# def maxSubArray(nums):
#     n = len(nums)
#     max_sum = -10000

#     for i in range(0, n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum = current_sum + nums[j]
#             if current_sum > max_sum:
#                 max_sum = current_sum
    
#     return max_sum

def maxSubArray(nums):
    max = nums[0]
    current_sum = 0

    for n in nums:
        current_sum += n
        if current_sum > max:
            max = current_sum
        if current_sum < 0:
            current_sum = 0
    
    return max
        
        
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))