# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        second = head
        ctr = 0
        while ctr < n:
            second = second.next
            ctr += 1
        
        first = dummy

        while second:
            first = first.next
            second = second.next
        
        if first.next:
            first.next = first.next.next
        
        return dummy.next