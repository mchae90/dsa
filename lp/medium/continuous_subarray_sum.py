class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        hmap = {0: -1}
        count = 0
        for i, n in enumerate(nums):
            count += n
            r = count % k

            if r not in hmap:
                hmap[r] = i
            
            else:
                if i - hmap[r] > 1:
                    return True

        return False

