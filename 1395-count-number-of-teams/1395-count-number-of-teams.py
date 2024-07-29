class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating) - 1):
            left_greater, left_smaller = 0, 0
            right_greater, right_smaller = 0, 0

            for j in range(i-1, -1, -1):
                if rating[j] < rating[i]:
                    left_smaller += 1
                else:
                    left_greater += 1
            
            for j in range(i+1, len(rating)):
                if rating[j] < rating[i]:
                    right_smaller += 1
                else:
                    right_greater += 1

            res += (left_smaller * right_greater) + (left_greater * right_smaller)
        
        return res