# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()
        q.append(root)

        if not root:
            return []

        while q:
            for i in range(len(q)):
                pop = q.popleft()
                if pop.right:
                    q.append(pop.right)
                if pop.left:
                    q.append(pop.left)
                if i == 0:
                    res.append(pop.val)            

        return res