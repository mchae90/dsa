# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        s, f = dummy, dummy

        for i in range(n):
            f = f.next

        while f.next:
            s = s.next
            f = f.next
        
        s.next = s.next.next

        return dummy.next


# BRUTE FORCE
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        hmap = {}

        cur = dummy
        count = 0
        while cur:
            hmap[count] = cur
            count +=1
            cur = cur.next
        

        hmap[max(hmap.keys()) - n].next = hmap[max(hmap.keys()) - n].next.next

        return dummy.next
    
# TC: O(n)
# SC: O(n)