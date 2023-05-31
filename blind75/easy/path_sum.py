# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
                
        def dfs(root, sum):
            if not root:
                return False
            sum += root.val
            
            # if current node is leaf node
            if not root.left and not root.right:
                if sum == targetSum:
                    return True
            
            left = dfs(root.left, sum)
            right = dfs(root.right, sum)
            
            if left or right:
                return True
            return False
        
        return dfs(root, 0)