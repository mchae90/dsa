class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] != 1:
                return 0
            
            visited.add((r,c))
            
            total = 1

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                total += dfs(nr, nc)
            
            return total

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res = max(res, dfs(r,c))

        return res
        

        # TC: O(m * n)
        # SC: O(m * n)
