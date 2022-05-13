from pip import List


# def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums, target):
    nums_dict = {}

    for i in range(len(nums)):
        # if difference in hash map, 
        diff = target - nums[i]
        if diff in nums_dict:
            print(i, nums_dict[diff])
            return [i, nums_dict[diff]]
        else:
            nums_dict[nums[i]] = i


    # [2,7,5,1] 
    # target = 6
    # answer = [2,3]

    # [1,2,4,4,9]
    # target = 8

    # hash map {2:0, 7:1, 5:2, 1:3}
    # hash map {0:2, 1:7, 2:5, 3:1}

twoSum([2,7,5,1], 6)