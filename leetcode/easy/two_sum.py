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
        diff = target - nums[i]
        if diff in hash_map:
            return [i, hash_map[diff]]
        else:
            hash_map[nums[i]] = i

# Key - Take difference between target and current item in nums array.  Check if in hash map.  
# If yes, return current index and comp's index.  
# If no, push to hash map {hash_map[nums[i]]: i}
# Important: store the value as key and index as value.  This will allow you to return the two indexes as answer more easily
# If you store in the dict the other way around, it will be more difficult to return the indexes, resulting in larger TC

# SC O(n)
# TC O(n)