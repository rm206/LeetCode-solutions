# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        dummy = ListNode(0, head)
        stack.append(dummy)

        while curr:
            while curr.val > stack[-1].val and stack[-1] != dummy:
                stack.pop()
            stack[-1].next = curr
            stack.append(curr)
            curr = curr.next
        
        return dummy.next