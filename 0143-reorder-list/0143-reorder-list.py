# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse_list(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy
            turn = 1
            
            while l1 and l2:
                if turn == 1:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
                turn *= -1
            
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
                
            return dummy.next
            
        if not head.next:
            return head
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None
        l1 = head
        
        l2 = reverse_list(l2)
        l1 = merge(l1, l2)
        head = l1