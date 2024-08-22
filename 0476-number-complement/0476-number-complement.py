class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        
        cnt = 0
        while temp != 0:
            temp = temp >> 1
            cnt += 1
        
        mask = 0
        while cnt:
            mask = mask << 1
            mask = mask + 1
            cnt -= 1
        
        return ~num & mask