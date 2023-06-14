# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            if curr_sum > 9:
                node_val = curr_sum - 10
                carry = 1
            else:
                node_val = curr_sum
                carry = 0
            
            curr.next = ListNode(node_val, None)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr_sum = l1.val + carry
            if curr_sum > 9:
                node_val = curr_sum - 10
                carry = 1
            else:
                node_val = curr_sum
                carry = 0
            curr.next = ListNode(node_val, None)
            curr = curr.next
            l1 = l1.next
        
        while l2:
            curr_sum = l2.val + carry
            if curr_sum > 9:
                node_val = curr_sum - 10
                carry = 1
            else:
                node_val = curr_sum
                carry = 0
            curr.next = ListNode(node_val, None)
            curr = curr.next
            l2 = l2.next
        
        if carry:
            curr.next = ListNode(1, None)
        
        return dummy.next