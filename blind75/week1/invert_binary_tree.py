# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
        
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root

# Recursively switch root note, only running if root is not null
# TC: O(n)
# SC: O(h) (h being max depth of tree)