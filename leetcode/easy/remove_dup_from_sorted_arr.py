# LC 26

def remove_dup_from_sorted_arr(nums):
    lp = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[lp] = nums[i]
            lp += 1
    return lp