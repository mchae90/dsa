# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def printList(self):
#         temp = self.data
#         while temp:
#             print (temp.data)
#             temp = temp.next
    
# def count_nodes(head):
#     count = 1
#     current = head
#     while current.next is not None:
#         current = current.next
#         count += 1
#     return count

# # nodeA = Node(6)
# # nodeB = Node(3)
# # nodeC = Node(4)
# # nodeD = Node(2)
# # nodeE = Node(1)

# # nodeA.next = nodeB
# # nodeB.next = nodeC
# # nodeC.next = nodeD
# # nodeD.next = nodeE

# # print("This linked list's length is: (should print 5)")
# # print(count_nodes(nodeA))



# llist = LinkedList()

# list.head = Node(1)
# second = Node(2)
# third = Node(3)

# list.head.next = second
# second.next = third

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next!= None:
            current = current.next
        current.next = new_node

    def length(self):
        count = 0
        current = self.head
        while current.next!=None:
            count +=1
            current = current.next
        return count
    
    def display(self):
        elements = []
        current = self.head
        while current.next!=None:
            current = current.next
            elements.append(current.data)
        print(elements)

    def get(self, index):
        if index > self.length():
            print('invalid index')
            return None
        current = self.head
        for x in range(index):
            current = current.next
        return current.data

    def erase(self, index):
        if index > self.length():
            print('invalid index')
            return None
        current_node = self.head
        current_index = 0
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

ll.display()
print(ll.get(5))

ll.erase(2)
ll.display()