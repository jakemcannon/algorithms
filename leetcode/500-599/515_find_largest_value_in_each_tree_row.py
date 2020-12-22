class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        result = []
        q = collections.deque()
        q.append(root)
        result.append(root.val)
        
        while q:
            row = []
            row_length = len(q)
            for i in range(row_length):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    row.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    row.append(cur.right.val)
            if row:
                m = max(row)
                result.append(m)

            
        return result