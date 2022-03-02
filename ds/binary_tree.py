class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)

root = Node(10)
root.left = Node(7)
root.left.left = Node(6)
root.left.left.left = Node(1)
root.left.right = Node(8)
root.left.right.right = Node(9)

root.right = Node(11)
root.right.right = Node(20)
root.right.right.left = Node(14)
root.right.right.right = Node(22)


print(post_order_traversal(root))