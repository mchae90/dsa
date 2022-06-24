from collections import deque

def bfs2d(list):
    m = len(list)
    n = len(list[0])
    visited = set()
    q = deque()

    dCol = [0, 0, -1, 0, 1]
    dRow = [0, 1, 0, -1, 0]

    q.append((0,0))
    
    while q:
        (i, j) = q.popleft()
        for k in range(5):
            shift_column = i + dCol[k]
            shift_row = j + dRow[k]
            if 0 <= shift_column < m and 0 <= shift_row < n and (shift_column, shift_row) not in visited:
                print((i,j), list[shift_column][shift_row])
                visited.add((shift_column, shift_row))
                q.append((shift_column, shift_row))

print(bfs2d([[1,2,3],[4,5,6],[7,8,9]]))