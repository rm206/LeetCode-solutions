# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, left, right):
            if not node:
                return True
            elif not (node.val > left and node.val < right):
                return False
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)
        
        return helper(root, float("-inf"), float("inf"))        

'''
        res = []
        
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        
        helper(root)
        print(res)
        if len(res) < 2:
            return True
        
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        
        return True
'''