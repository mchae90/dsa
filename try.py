from collections import deque

def updateMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    
    q = deque()
    
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
            else:
                mat[i][j] = -1
    
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    
    while q:
        # print(q)
        (x, y) = q.pop()
        
        for k in range(4):
            shift_row = x + d_row[k]
            shift_col = y + d_col[k]
            if 0 <= shift_row < m and 0 <= shift_col < n and mat[shift_row][shift_col] == -1:
                print(shift_row, shift_col, mat[shift_row][shift_col])

                # print('update', (x,y))
                # print('orig', (i, j), 'shifted', (shift_col, shift_row), 'mat[shift_col][shift_row]', mat[shift_col][shift_row],  'mat[i][j]+1', mat[i][j] + 1)
                mat[shift_row][shift_col] = mat[x][y] + 1
                # print('orig', (i, j), 'shifted', (shift_col, shift_row), 'mat[shift_col][shift_row]', mat[shift_col][shift_row],  'mat[i][j]+1', mat[i][j] + 1)
                q.append((shift_row, shift_col))
                # print()


    return mat

print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))