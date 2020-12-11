class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result = [] 
        if not root:
            return result
        
        q = collections.deque()
        q.append(root)
        j = 0
        while q:
            level = []
            level_len = len(q)
            for i in range(level_len):
                root = q.popleft()
                level.append(root.val)
                
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                    
            # this might be more optimized
            # than having the for loop after the bfs traversal
            if j % 2 != 0:
                level = level[::-1]
            result.append(level)
            j+=1
            
        # go through the final result and reverse the odd entries
        # for i in range(len(result)):
        #     if i % 2 != 0:
        #         result[i] = result[i][::-1]
            
        return result 