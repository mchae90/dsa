def contains_dup(nums):
    nums_set = set()
    for i in nums:
        if i in nums_set:
            return True
        nums_set.add(i)
    return False

contains_dup([1,1,1,3,3,4,3,2,4,2])

# Multiple ways to solve this.
# 1) Brute force - nested for loop - TC: O(n^2), SC: O(1)
# 2) Sort the array - TC: O(n*log(n)), SC: O(1)
# 3) Use Hash Set (best) - TC: O(n), SC: O(n)