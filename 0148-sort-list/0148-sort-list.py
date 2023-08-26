# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def helper(head):
            def get_mid(head):
                slow, fast = head, head.next
                while fast and fast.next:
                    slow = slow.next
                    fast = fast.next.next
                
                return slow
            
            def merge(p1, p2):
                dummy = ListNode()
                curr = dummy
                
                while p1 or p2:
                    v1 = p1.val if p1 else float('inf')
                    v2 = p2.val if p2 else float('inf')
                    
                    if v1 < v2:
                        curr.next = p1
                        p1 = p1.next
                    else:
                        curr.next = p2
                        p2 = p2.next
                    curr = curr.next
                
                return dummy.next
                
            if not head or not head.next:
                return head
            
            mid = get_mid(head)
            
            left = head
            right = mid.next
            mid.next = None
            
            left = helper(left)
            right = helper(right)
            
            new_head = merge(left, right)
            return new_head
            
        
        res = helper(head)
        return res