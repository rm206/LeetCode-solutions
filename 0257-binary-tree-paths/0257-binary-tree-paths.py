# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, curr):
            curr.append(str(node.val))
            
            if not node.left and not node.right:
                res.append(curr.copy())

            
            else:
                if node.left:
                    dfs(node.left, curr)
                
                if node.right:
                    dfs(node.right, curr)
            
            curr.pop()
            
        res = []
        curr = []
        dfs(root, curr)
        res = ["->".join(x) for x in res]
        return res