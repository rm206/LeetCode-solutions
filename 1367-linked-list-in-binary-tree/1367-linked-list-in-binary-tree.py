# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def match(ll, tree):
            if not ll:
                return True
            
            if not tree:
                return False
            
            if ll.val != tree.val:
                return False
            
            return match(ll.next, tree.left) or match(ll.next, tree.right)
        
        def solver(ll, tree):
            if not tree:
                return False
            
            if match(ll, tree):
                return True
            
            return solver(ll, tree.left) or solver(ll, tree.right)
        
        return solver(head, root)