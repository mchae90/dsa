class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        # Define counters for word and board
        countB = Counter()
        countW = Counter(word)

        for i in range(rows):
            for j in range(cols):
                    countB[board[i][j]] += 1

        # if a character in word not in board OR character in word appears more than board, return False immediately
        for character, count in countW.items():
            if character not in countB:
                return False
            if countB[character] < count:
                return False

        def dfs(r,c, i):
            # base cases
            # if we make it past len(word), we obviously found the answer, so return True
            if i >= len(word):
                return True
            # if out of bounds, or already visited or the board character doesn't match current word character
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or board[r][c] != word[i]:
                return False

            # makes it past the base cases, so we will visit this cell
            visited.add((r,c))

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # if any of neighbors return True, then we found a matching word path, so return True
                if dfs(nr, nc, i + 1):
                    return True
            
            # need to remove all visited for this cell's DFS
            visited.remove((r,c))

            # if at the end of DFS, we still haven't returned True, return False
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    # only if this cell returns true, return true for whole matrix
                    # else, we still need to iterate through the entire matrix to find the potential word
                    if dfs(r,c, 0):
                        return True
        
        return False
    
    # TC: O(m * n * dfs) -> O(m * n * 4^n)
    # SC: O(m * n)