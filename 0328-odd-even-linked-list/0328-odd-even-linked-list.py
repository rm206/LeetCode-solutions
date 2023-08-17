# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy, even_dummy = ListNode(0, None), ListNode(0, None)
        odd, even = odd_dummy, even_dummy
        curr = head
        index = 1
        
        while curr:
            if index % 2 != 0:
                odd.next = curr
                odd = odd.next
                curr = curr.next
            else:
                even.next = curr
                even = even.next
                curr = curr.next
            index += 1
        
        even.next = None
        odd.next = even_dummy.next
        
        return odd_dummy.next