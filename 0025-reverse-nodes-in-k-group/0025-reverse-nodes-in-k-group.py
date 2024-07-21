# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        
        if cnt < k:
            return head
        
        cnt = 0
        curr = head
        prev = None
        nxt = None
        while curr and cnt < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            cnt += 1

        if nxt:
            head.next = self.reverseKGroup(nxt, k)
        
        return prev