class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        if not root:
            return []
        
        result = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            
            temp = 0
            level_length = len(q)
            for i in range(level_length):
                
                root = q.popleft()
                temp += root.val
                
                if root.left:
                    q.append(root.left)
                    
                if root.right:
                    q.append(root.right)
                    
            result.append(temp / level_length)
            
        return result