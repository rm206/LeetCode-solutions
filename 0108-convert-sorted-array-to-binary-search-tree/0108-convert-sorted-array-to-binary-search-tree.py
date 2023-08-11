# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(arr):

            if len(arr) == 1:
                return TreeNode(arr[0])

            mid = len(arr) // 2
            
            left = build(arr[:mid])
            
            if mid + 1 < len(arr):
                right = build(arr[mid+1:])
            else:
                right = None
                
            root = TreeNode(arr[mid], left, right)
            return root

        root = build(nums)
        return root
