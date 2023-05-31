# Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if not root:
            return

        res = []
        stack = [root]

        while stack:
            cur = stack.pop()
            if cur.children:
                stack.extend(cur.children[::-1])
            res.append(cur.val)
            
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


