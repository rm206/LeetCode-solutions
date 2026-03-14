class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(curr):
            nonlocal ctr, res
            if res:
                return

            if len(curr) == n:
                ctr += 1
                if ctr == k:
                    res = "".join(curr)
                return
            
            for ch in chars:
                if not curr or ch != curr[-1]:
                    curr.append(ch)
                    dfs(curr)
                    curr.pop()

        chars = ["a", "b", "c"]
        res = ""
        ctr = 0
        dfs([])
        return res