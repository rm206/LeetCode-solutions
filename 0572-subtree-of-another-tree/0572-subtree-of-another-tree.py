# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(s, t):
            if not s and not t:
                return True
            
            if (s and not t) or (not s and t):
                return False
            
            return s.val == t.val and is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)
        
        if not subRoot and root:
            return True
        
        elif subRoot and not root:
            return False
        
        return is_same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

'''
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    if not subRoot and root:
        return True

    elif subRoot and not root:
        return False

    return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

def isSameTree(self, s, t):

    if not s and not t:
        return True

    elif (not s and t) or (s and not t):
        return False

    else:
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
'''