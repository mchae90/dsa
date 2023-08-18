# PREORDER

# iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        stack.append(root)
        res = []

        while stack:
            pop = stack.pop()

            if pop:
                res.append(pop.val)
                stack.append(pop.right)
                stack.append(pop.left)

        return res

# recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res
    

# INORDER

# iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []

        cur = root

        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            if not stack:
                return res
            
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return res
    
# POSTORDER

# iterative


# recursive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        
        dfs(root)
        
        return res