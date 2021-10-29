class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert(root, key):
    # if root is none, create new node with given key
    if root is None:
        return Node(key)
    else:
        
        if root.key == key:
            return root
        elif root.key < key:
            root.right 
fd