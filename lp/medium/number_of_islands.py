# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        hset = set()
        islands = 0

        def dfs(r, c):
            if (r not in range(rows)) or (c not in range(cols)) or grid[r][c] == "0" or (r, c) in hset:
                return
            
            hset.add((r, c))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in hset and grid[i][j] != "0":
                    islands += 1
                    dfs(i, j)
        
        return islands
    
# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        hset = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            hset.add((r, c))

            while q:
                row, col = q.popleft()

                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr in range(rows)) and (nc in range(cols)) and grid[nr][nc] == "1" and (nr, nc) not in hset:
                        q.append((nr, nc))
                        hset.add((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in hset and grid[i][j] != "0":
                    islands += 1
                    bfs(i, j)
        
        return islands