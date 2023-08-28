# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not k:
            return head
        
        len_list = 0
        p = head
        last_node = None
        while p:
            len_list += 1
            last_node = p
            p = p.next
        
        k = k % len_list
        
        last_node.next = head
        
        temp_node = head
        for i in range(len_list - k - 1):
            temp_node = temp_node.next
            k -= 1
        
        res = temp_node.next
        temp_node.next = None
        
        return res