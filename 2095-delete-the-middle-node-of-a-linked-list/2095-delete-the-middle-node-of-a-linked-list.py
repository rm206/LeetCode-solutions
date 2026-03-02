# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        dummy = ListNode(-1, head)
        first, slow, fast = dummy, head, head

        while fast and fast.next:
            first = first.next
            slow = slow.next
            fast = fast.next.next
        
        first.next = first.next.next
        return dummy.next
