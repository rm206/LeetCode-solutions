# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node):
            if not node or not node.next:
                return node
            
            newhead = rev(node.next)
            node.next.next = node
            node.next = None
            return newhead
        
        return rev(head)