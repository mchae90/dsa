from typing import List

def twoSum(nums, target):
    for x in range(0, len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]

twoSum([2,7,11,15], 9)

def twoSum2(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in hash_map:
            return [i, hash_map[comp]]
        else:
            hash_map[nums[i]] = i