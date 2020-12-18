class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        max_depth = 0
        q = collections.deque()
        q.append(root)
        
        while q:
            
            level_length = len(q)
            
            for _ in range(level_length):
                
                root = q.popleft()
                
                for child in root.children:
                    q.append(child)
                    
            max_depth+=1
            
        return max_depth