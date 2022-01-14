# LC 83

def delete_duplicates(head):
    current = head
    
    while current:

        while current.next != None and current.next.val == current.val:
            current.next = current.next.next

        current = current.next

    return head

