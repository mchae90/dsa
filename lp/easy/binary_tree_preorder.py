# Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

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

# Recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, n, res):
        if not n:
            return None
        res.append(n.val)
        
        for i in n.children:
            self.dfs(i, res)


