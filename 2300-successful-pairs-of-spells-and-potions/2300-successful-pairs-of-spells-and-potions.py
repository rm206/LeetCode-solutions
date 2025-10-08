"""
mapping = defaultdict(list)
for i, s in enumerate(spells):
    mapping[s].append(i)

spells.sort()
potions.sort()
len_potions = len(potions)
pairs = [0] * len(spells)

min_index_found = len_potions - 1

for s in spells:
    while min_index_found >= 0 and s * potions[min_index_found] >= success:
        min_index_found -= 1
    
    pairs[mapping[s][-1]] = len_potions-min_index_found-1
    mapping[s].pop()

return pairs
"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def matches(val):
            l, r = 0, len(potions) - 1
            res = None
            while l <= r:
                mid = (l + r) // 2

                if potions[mid] * val >= success:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            if res is None:
                return 0
            
            return len(potions) - res

        pairs = [0] * len(spells)
        potions.sort()

        for i, s in enumerate(spells):
            pairs[i] = matches(s)
        
        return pairs