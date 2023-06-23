class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    counter += 1
                    flowerbed[i] = 1
        
        return counter >= n