# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        dummy = ListNode(-1, head)

        prev = dummy
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next