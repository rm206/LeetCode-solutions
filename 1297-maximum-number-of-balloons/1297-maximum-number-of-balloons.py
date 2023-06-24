class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = 0
        m = {}

        for t in text:
            if t in "balon":
                m[t] = 1 + m.get(t, 0)
        
        if ('b' in m) and ('a' in m) and ('l' in m) and ('o' in m) and ('n' in m):
            out_of_letters = False
            while not out_of_letters:
                if m['b'] >= 1 and m['a'] >= 1 and m['l'] >= 2 and m['o'] >= 2 and m['n'] >= 1:
                    res += 1
                    m['b'] -= 1
                    m['a'] -= 1
                    m['l'] -= 2
                    m['o'] -= 2
                    m['n'] -= 1
                else:
                    out_of_letters = True
        
        return res