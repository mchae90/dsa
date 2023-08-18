# Recursive
def invert_tree(root):
    # base case
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    self.invert_tree(root.left)
    self.invert_tree(root.right)

    return root

# Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return
        
        q = deque()
        q.append(root)

        cur = root

        while q:
            for _ in range(len(q)):
                pop = q.popleft()

                pop.left, pop.right = pop.right, pop.left

                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
        
        return root
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        stack = []
        stack.append(root)

        while stack:
            pop = stack.pop()

            pop.left, pop.right = pop.right, pop.left

            if pop.left:
                stack.append(pop.left)
            if pop.right:
                stack.append(pop.right)
            

        return root