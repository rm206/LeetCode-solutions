# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list():
            prev, curr = None, head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev

        num = 0
        curr = head
        while curr:
            num = num*10 + curr.val
            curr = curr.next
        
        num = num * 2
        
        head = reverse_list()

        curr = head
        prev = None
        while curr:
            curr.val = num % 10
            prev = curr
            curr = curr.next
            num = num // 10
        
        while num:
            prev.next = ListNode(num % 10)
            prev = prev.next
            num = num // 10
        
        head = reverse_list()

        return head