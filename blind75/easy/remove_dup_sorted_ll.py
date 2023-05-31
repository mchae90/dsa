# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        tail.next = head
        
        cur_val = None
        
        while tail and tail.next:
            if tail.next.val != cur_val:
                tail = tail.next
                cur_val = tail.val
            
            else:
                temp = tail.next
                while temp.next and temp.next.val == cur_val:
                    temp = temp.next
                tail.next = temp.next
                
            
        
        return dummy.next