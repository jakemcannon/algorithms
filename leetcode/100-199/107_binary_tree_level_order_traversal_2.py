class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        result = []
        
        if not root:
            return result
        
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            level_len = len(q)
            for _ in range(level_len):
                
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            result.append(level)
        
        return result[::-1]