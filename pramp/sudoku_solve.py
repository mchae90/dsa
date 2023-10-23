def backtrack(board, row, col):
  """ Returns bool """
  if row == 9:
    return True

  if col == 9:
    return backtrack(row+1, 0)

  if board[row][col] != ".":
    return backtrack(row, col+1)
  
  for val in range(1, 10):
    if val in row_set[row]:
      continue
    
    if val in col_set[col]:
      continue
    
    if val in cube_set[(row//3, col//3)]:
      continue
    
    board[row][col] = val
    row_set[row].add(val)
    col_set[col].add(val)
    cube_set[(row//3, col//3)].add(val)
    
    if backtrack(board, row, col+1):
      return True
    
    board[row][col] = "."
    row_set[row].remove(val)
    col_set[col].remove(val)
    cube_set[(row//3, col//3)].remove(val)

  return False

def sudoku_solve(board):
  '''
  row: {
  0: set(),
  1: set()
  }
  col: {
    0: set(),
    1: set(),
  }
  
  cube: {
    (0,0): set(),
    (0,1): set(7),
  }
  
  (0, 4)
  (0, 1)
  
  '''

  row_set = { i: set() for i in range(9)}
  col_set = { i: set() for i in range(9)}
  cube_set = { (i, j): set() for i in range(3) for j in range(3)}

  for r in range(9):
    for c in range(9):
      value = board[r][c]
      row_set[r].add(value)
      col_set[c].add(value)
      cube_set[(r//3,c//3)].add(value)
  
  return backtrack(board, 0, 0)

"""
https://leetcode.com/problems/sudoku-solver/editorial/

https://leetcode.com/problems/valid-sudoku/
"""
