
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    
    q = collections.deque()
    q.append(root)
    
    while q:
        level = []
        level_length = len(q)
        for i in range(level_length):
            node = q.popleft()
            level.append(node.val)
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
        result.append(level)
        
    return result