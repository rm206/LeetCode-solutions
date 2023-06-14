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
        
        while l1 or l2 or carry:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            curr_sum = v1 + v2 + carry
            carry = curr_sum // 10
            val = curr_sum % 10
            
            curr.next = ListNode(val)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        


'''
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
'''