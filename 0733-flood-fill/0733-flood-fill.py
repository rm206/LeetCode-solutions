class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def solver(sr, sc, color, parent):
            if sr < 0 or sr >= m or sc < 0 or sc >= n:
                return
            if image[sr][sc] == color:
                return
            
            if image[sr][sc] != parent:
                return
            
            image[sr][sc] = color
            
            solver(sr - 1, sc, color, parent)
            solver(sr + 1, sc, color, parent)
            solver(sr, sc - 1, color, parent)
            solver(sr, sc + 1, color, parent)
        
        
        m, n = len(image), len(image[0])
        parent = image[sr][sc]
        solver(sr, sc, color, parent)
        return image