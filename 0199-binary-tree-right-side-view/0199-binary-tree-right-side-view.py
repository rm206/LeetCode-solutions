# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.res = []
        
        def helper(node):
            q = []
            q.append(node)
            
            while len(q) != 0:
                qlen = len(q)
                level = []
                
                for i in range(qlen):
                    n = q.pop(0)
                    if n:
                        level.append(n.val)
                        q.append(n.left)
                        q.append(n.right)
                if level:
                    self.res.append(level[-1])                
        
        helper(root)
        return self.res