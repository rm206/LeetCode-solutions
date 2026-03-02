# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head, even_head = ListNode(-1), ListNode(-1)
        curr = head
        odd_curr, even_curr = odd_head, even_head

        flag = 1
        while curr:
            if flag == 1:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            if flag == -1:
                even_curr.next = curr
                even_curr = even_curr.next
            
            curr = curr.next
            flag *= -1
        
        even_curr.next = None
        odd_curr.next = even_head.next

        return odd_head.next