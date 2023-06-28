def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    target_val = image[sr][sc]
    max_sr = len(image)
    max_sc = len(image[0])

    def dfs(sr, sc):
        if 0 <= sr < max_sr and 0 <= sc < max_sc and image[sr][sc] == target_val and image[sr][sc] != newColor:
            image[sr][sc] = newColor

            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)
    
    dfs(sr, sc)

    return image

    # Key: DFS on 4 directions surrounding starting pixel.  Must bound sr and sc (min: 0, max: length).
    # Call recursively for the 4 pixels surrounding
    # TC: O(n): n is number of pixels
    # SC: O(n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or image[r][c] != original or image[r][c] == color:
                return
            image[r][c] = color

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image
    
