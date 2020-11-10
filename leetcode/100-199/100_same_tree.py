def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
    if not p and not q:
        return True
    elif not p and q:
        return False
    elif p and not q:
        return False
    
    if p.val != q.val:
        return False
    
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)