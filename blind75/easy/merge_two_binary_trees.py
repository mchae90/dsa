# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not p and not q:
            return

        if not p:
            return q

        if not q:
            return p

        root = TreeNode(p.val + q.val)
    
        root.left = self.mergeTrees(p.left, q.left)
        root.right = self.mergeTrees(p.right, q.right)
        
        return root

# Define base cases.
# If base cases are not met, that means p and q are not null.
# Define root, assign left and right values recursively.
# Return root