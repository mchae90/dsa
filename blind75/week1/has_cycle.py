def hasCycle(head):
    s, f = head, head
    
    while f and f.next:
        s = s.next
        f = f.next.next
        
        if s == f:
            return True
    
    return False

# TC: O(n)
# SC: O(1)