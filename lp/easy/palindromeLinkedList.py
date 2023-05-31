# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        
        while f and f.next:
            s = s.next
            f = f.next.next
        
        prev = None
        
        while s:
            temp = s.next
            s.next = prev
            prev = s
            s = temp
        
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True

TC: O(n)
SC: O(1)