class Solution:
    def floodFillHelper(self, image, sr, sc, new_color, original_color):
        if (sr < 0) or (sr > len(image) - 1) or (sc < 0) or (sc > len(image[0]) - 1) or (image[sr][sc] != original_color):
            return
        
        image[sr][sc] = new_color
        self.floodFillHelper(image, sr-1, sc, new_color, original_color)
        self.floodFillHelper(image, sr+1, sc, new_color, original_color)
        self.floodFillHelper(image, sr, sc-1, new_color, original_color)
        self.floodFillHelper(image, sr, sc+1, new_color, original_color)
        
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        self.floodFillHelper(image, sr, sc, color, image[sr][sc])
        return image