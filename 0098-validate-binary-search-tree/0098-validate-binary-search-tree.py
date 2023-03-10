# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidHelper(self, root: Optional[TreeNode], left, right):
        if not root:
            return True
        if not(root.val < right and root.val > left):
            return False
        return self.isValidHelper(root.left, left, root.val) and self.isValidHelper(root.right, root.val, right)
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidHelper(root, float("-inf"), float("inf"))

'''
T: O(N) S: O(H+N)
    def isValidHelper(self, root: Optional[TreeNode], arr):
        if root:
            self.isValidHelper(root.left, arr)
            arr.append(root.val)
            self.isValidHelper(root.right, arr)
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inOrder = []
        self.isValidHelper(root, inOrder)
        for i in range(len(inOrder) - 1):
            if inOrder[i] >= inOrder[i+1]:
                return False
        return True
'''