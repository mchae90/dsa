# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head
        intersection = None

        while f and f.next:
            s = s.next
            f = f.next.next

            if s == f:
                intersection = s
                break
        
        if intersection == None:
            return None
        
        s2 = head

        while s2 != intersection:
            s2 = s2.next
            intersection = intersection.next

        return s2
