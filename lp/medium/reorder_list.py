# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # calculate midpoint
        s, f = head, head

        while f.next and f.next.next:
            s = s.next
            f = f.next.next

        # reverse second half
        prev = None
        cur = s
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        s.next = None

        h1, h2 = head, prev

        while h1 and h2:
            h1n = h1.next
            h2n = h2.next

            h1.next = h2
            h1 = h1n

            h2.next = h1
            h2 = h2n
        