class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        q = collections.deque()
        q.append(root)
        
        
        while q:
            
            level = []
            level_length = len(q)
            
            for _ in range(level_length):
                
                root = q.popleft()
                
                if root.left:
                    q.append(root.left)
                    level.append(root.left.val)
                    
                if not root.left:
                    level.append(None)
                
                if root.right:
                    q.append(root.right)
                    level.append(root.right.val)
                    
                if not root.right:
                    level.append(None)
            
            p1, p2 = 0, len(level)-1
            while p1 < p2:
                if level[p1] != level[p2]:
                    return False
                p1+=1
                p2-=1
        return True