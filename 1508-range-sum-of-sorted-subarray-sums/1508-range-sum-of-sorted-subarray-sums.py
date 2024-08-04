class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = []

        for i in range(n):
            tsum = 0
            for j in range(i, n):
                tsum += nums[j]
                temp.append(tsum)

        temp.sort()
        
        return sum(temp[left-1:right]) % (10**9 + 7)