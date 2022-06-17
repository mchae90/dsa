def isBalanced(root):

    def dfs(root):
        # base case: if node is None
        if not root:
            return 0
        
        left, right = dfs(root.left), dfs(root.right)

        balanced = abs(left - right) <= 1

        if not balanced:
            return False
        