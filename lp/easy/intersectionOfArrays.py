class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        res = []
        for n in set1:
            if n in set2:
                res.append(n)

        return res
    
    # TC: O(n)
    # SC: O(m + n)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for n1 in nums1:
            if n1 in nums2 and n1 not in res:
                res.append(n1)

        return res
    
    # TC: O(n^2)
    # SC: O(n)