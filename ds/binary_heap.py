from collections import deque

class MaxHeap:
    def __init__(self):
        self.list = deque()
    


    

root = Node(2)
root.left = Node(4)
root.left.left = Node(9)
root.left.left.left = Node(15)
root.left.left.right = Node(20)

root.left.right = Node(7)
root.left.right.left = Node(13)

root.right = Node(8)
root.right.left = Node(10)
root.right.right = Node(9)
