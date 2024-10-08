from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            while q[0] < r-k+1:
                q.popleft()
                l += 1
            
            if r >= k - 1:
                res.append(nums[q[0]])
        
        return res