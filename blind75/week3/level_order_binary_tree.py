# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            cur_lev = []
            for n in range(len(q)):
                pop = q.popleft()
                cur_lev.append(pop.val) 
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            res.append(cur_lev)
        return res

# Key: Use queue.  Append root.  Popleft root and append children (left then right) in a while loop
# TC: O(n)