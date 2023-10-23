from collections import deque

def shortestCellPath(grid, sr, sc, tr, tc):
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    q = deque()
    q.append((sr, sc))

    count = 0

    while q:
        for i in range(len(q)):
            cur = q.popleft()
            print(cur)
            r, c = cur[0], cur[1]

            visited.add((r, c))

            if cur == (tr, tc):
                return count

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for dr, dc in directions:
                nr = cur[0] + dr
                nc = cur[1] + dc

                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    print(nr, nc)
                    q.append((nr, nc))

        count += 1

    return -1

print(shortestCellPath([[1,1,1,1],[0,0,0,1],[1,1,1,1]], 0, 0, 2, 0))