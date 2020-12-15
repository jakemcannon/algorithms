class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        result = []
        
        q = collections.deque()
        q.append(root)
        
        while q:

            level_length = len(q)
            for i in range(level_length):
                root = q.popleft()
                
                if i == 0:
                    result.append(root.val)
                    
                if root.right:
                    q.append(root.right)
                    
                if root.left:
                    q.append(root.left)
                    
        return result