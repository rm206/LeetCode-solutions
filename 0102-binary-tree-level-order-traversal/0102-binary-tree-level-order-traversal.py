# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, depth, arr):
        if root is None:
            return
        arr[depth].append(root.val)
        self.helper(root.left, depth+1, arr)
        self.helper(root.right, depth+1, arr)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a = [[] for _ in range(2000)]
        self.helper(root, 0, a)
        a = [x for x in a if x != []]
        return a