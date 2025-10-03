class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        cand = None

        for n in nums:
            if not cand:
                cand = n
                freq = 1
            
            elif n == cand:
                freq += 1
            
            else:
                freq -= 1
                if freq == 0:
                    cand = n
                    freq = 1
        
        return cand