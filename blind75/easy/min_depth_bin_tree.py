# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        depth = 1
        
        q = deque([root])
        
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                
                if not n.left and not n.right:
                    return depth
                
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            
            depth += 1
            
        return depth

# DFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        # Edge case for when tree is skewed (if root.left or root.right is None, return max of either subtree)
        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

