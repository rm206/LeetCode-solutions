# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def solver(node, curr, run_sum):
            if not node:
                return
            
            curr.append(node.val)
            run_sum += node.val
            
            solver(node.left, curr, run_sum)
            solver(node.right, curr, run_sum)
            
            if not node.left and not node.right:
                if run_sum == targetSum:
                    res.append(curr.copy())
            
            curr.pop()
            run_sum -= node.val
        
        res = []
        curr = []
        run_sum = 0
        solver(root, curr, run_sum)
        
        return res