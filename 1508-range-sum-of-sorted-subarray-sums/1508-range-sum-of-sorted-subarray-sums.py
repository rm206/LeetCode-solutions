class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = []

        for i in range(n):
            tsum = nums[i]
            temp.append(tsum)
            for j in range(i+1, n):
                tsum += nums[j]
                temp.append(tsum)

        temp.sort()
        
        return sum(temp[left-1:right]) % (10**9 + 7)