# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            left_child = node.left
            right_child = node.right
            curr = left_child
            while curr.right:
                curr = curr.right
            curr.right = right_child
            return left_child

        if not root:
            return root
        
        dummy = TreeNode(math.inf, root)
        curr = dummy

        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = helper(curr.left)
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = helper(curr.right)
                else:
                    curr = curr.right
        
        return dummy.left