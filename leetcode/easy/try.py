

def try1(nums):
            
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]: 
                print(i, j)
    

try1([1,2,3,4,1])