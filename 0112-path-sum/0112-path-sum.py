# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, running_sum):
            if not root:
                return False
            running_sum += root.val
            if not root.left and not root.right:
                return running_sum == targetSum
            else:
                return (helper(root.left, running_sum) or helper(root.right, running_sum))
            
        
        return helper(root, 0)

'''
        sum_list = []
        
        def helper(root, running_sum):
            nonlocal sum_list
            
            if not root:
                return
            running_sum += root.val
            if not root.left and not root.right:
                sum_list.append(running_sum)
            else:
                helper(root.left, running_sum)
                helper(root.right, running_sum)
            
        
        helper(root, 0)
        return targetSum in sum_list
'''