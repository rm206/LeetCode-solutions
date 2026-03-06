class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        run_sum = sum(cardPoints[:k])
        res = run_sum
        l = k-1
        r = len(cardPoints)-1
        while l > -1:
            run_sum -= cardPoints[l]
            l -= 1
            run_sum += cardPoints[r]
            r -=1
            res = max(res, run_sum)
        
        return res