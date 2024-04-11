class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = [i for i in range(0, len(deck))]
        res = [None for i in range(len(deck))]
        deck.sort()
        
        for i in range(len(deck)):
            curr = q.pop(0)
            res[curr] = deck[i]
            
            if q:
                nxt = q.pop(0)
                q.append(nxt)
        
        return res