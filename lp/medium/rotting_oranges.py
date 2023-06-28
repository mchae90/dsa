class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = set()

        q = deque()
        minutes = 0

        has_fresh = False

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))

        if not fresh:
            return 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh.remove((nr, nc))
            minutes += 1
        
        if fresh:
            return -1
        return minutes - 1