# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#LNR

def in_order_traversal(root):
    res = []
    if root:
        in_order_traversal(root.left)
        res.append(root.val)
        in_order_traversal(root.right)
    return res