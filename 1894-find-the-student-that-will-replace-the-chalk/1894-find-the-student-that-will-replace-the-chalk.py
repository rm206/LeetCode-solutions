class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)

        # while k > s:
        #     k -= s
        k = k % s
        
        i = 0
        n = len(chalk)

        while True:
            index = i % n

            if k < chalk[index]:
                return i % n
            
            k -= chalk[index]
            i += 1