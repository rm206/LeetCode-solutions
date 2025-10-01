# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        temp = ListNode(0, head)

        second = head
        k = n
        while k:
            second = second.next
            k -= 1
        
        prev = temp

        while second:
            prev = prev.next
            second = second.next
        
        prev.next = prev.next.next

        return temp.next