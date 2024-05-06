class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        usual_max = max(candies)
        res = [False] * len(candies)
        for i, n in enumerate(candies):
            if n + extraCandies >= usual_max:
                res[i] = True
        
        return res