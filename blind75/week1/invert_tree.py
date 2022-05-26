from turtle import left, right


def invert_tree(root):
    # base case
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    self.invert_tree(root.left)
    self.invert_tree(root.right)

    return root