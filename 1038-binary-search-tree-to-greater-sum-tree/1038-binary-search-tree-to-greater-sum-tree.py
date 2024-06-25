# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_inorder(node):
            if not node:
                return
            
            reverse_inorder(node.right)
            nums.append(node.val)
            reverse_inorder(node.left)
        
        nums = []
        reverse_inorder(root)
        
        ctr = 0
        builder = []
        for n in nums:
            ctr += n
            builder.append(ctr)
        
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = builder[i]
        
        def process(node):
            if not node:
                return
            
            node.val = d[node.val]
            process(node.left)
            process(node.right)
        
        process(root)
        return root