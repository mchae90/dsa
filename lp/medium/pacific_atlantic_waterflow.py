class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pset = set()
        aset = set()
        
        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r not in range(rows) or c not in range(cols) or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pset, heights[0][c])
            dfs(rows - 1, c, aset, heights[rows - 1][c])
            
        for r in range(rows):
            dfs(r, 0, pset, heights[r][0])
            dfs(r, cols - 1, aset, heights[r][cols - 1])
            
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pset and (r, c) in aset:
                    res.append([r, c])
        
        return res