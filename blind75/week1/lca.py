# def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None

def lca(root, p, q):
    low = min(p.val, q.val)
    high = max(p.val, q.val)

    if low <= root.val <= high:
        return root

    if p < root and q < root:
        lca(root.left, p, q)
    else:
        lca(root.right, p, q)

# in LNR
# pre NLR
# post LRN