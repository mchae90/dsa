def isSameTree(self, p, q):
    # if both null
    if not p and not q:
        return True
    # both not null established.  only one of them null OR p and q are different values?
    if (not p or not q) or (p.val != q.val):
        return False

    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)