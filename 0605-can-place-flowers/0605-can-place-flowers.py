class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and n <= 1) or (flowerbed[0] == 1 and n == 0):
                return True
            else:
                return False
        
        counter = 0
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    counter += 1
                    flowerbed[i] = 1
                    
            if i == (len(flowerbed) - 1):
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    counter += 1
                    flowerbed[i] = 1
                
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    counter += 1
                    flowerbed[i] = 1
        
        return counter >= n
        
