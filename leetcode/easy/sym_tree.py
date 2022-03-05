def isSymmetric(self, root):
    cur_left = root.left
    cur_right = root.right

    if cur_left and cur_right:
        if cur_left.val == cur_right.val:
            
