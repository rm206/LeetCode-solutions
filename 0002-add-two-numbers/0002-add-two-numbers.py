# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

'''
        len_1, len_2 = 0, 0
        ptr_1, ptr_2 = l1, l2
        while ptr_1:
            len_1 += 1
            ptr_1 = ptr_1.next
        while ptr_2:
            len_2 += 1
            ptr_2 = ptr_2.next
        if len_1 > len_2:
            longer = l1
            shorter = l2
        else:
            longer = l2
            shorter = l1
        dummy = ListNode(0, longer)
        
        remainder = 0
        while longer or shorter:
            if shorter:
                curr_sum = longer.val + shorter.val + remainder
            else:
                curr_sum = longer.val + remainder
            if curr_sum >= 10:
                remainder = 1
                longer.val = curr_sum % 10
            else:
                remainder = 0
                longer.val = curr_sum
            
            if not longer.next:
                last_long = longer
            longer = longer.next
            if shorter:
                shorter = shorter.next
        
        if remainder == 1:
            last_long.next = ListNode(1, None)
        
        return dummy.next
'''
            