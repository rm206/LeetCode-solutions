class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        found = False
        while not found:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                found = True
        
        slow = 0
        slow2 = fast
        
        found = False
        while not found:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                return slow