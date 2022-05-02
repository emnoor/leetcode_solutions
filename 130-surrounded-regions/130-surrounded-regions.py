class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        if m < 3 or n < 3:
            return
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] != "O":
                    continue

                stack = [(i, j)]
                region = {(i, j)}
                # visit all neighbors to find regional points
                while stack:
                    ii, jj = stack.pop()
                    # top
                    if ii-1 >= 0 and board[ii-1][jj] == "O" and (ii-1, jj) not in region:
                        region.add((ii-1, jj))
                        stack.append((ii-1, jj))
                    # bottom
                    if ii+1 < m and board[ii+1][jj] == "O" and (ii+1, jj) not in region:
                        region.add((ii+1, jj))
                        stack.append((ii+1, jj))
                    # left
                    if jj-1 >= 0 and board[ii][jj-1] == "O" and (ii, jj-1) not in region:
                        region.add((ii, jj-1))
                        stack.append((ii, jj-1))
                    # right
                    if jj+1 < n and board[ii][jj+1] == "O" and (ii, jj+1) not in region:
                        region.add((ii, jj+1))
                        stack.append((ii, jj+1))
                    
                if all(ii>0 and jj>0 and ii<m-1 and jj<n-1 for (ii, jj) in region):
                    # region is surrounded
                    c = "X"
                else:
                    # region is not surrounded
                    # temporarily mark as Z so it won't be checked again
                    c = "Z"
                
                for (ii, jj) in region:
                    board[ii][jj] = c
                    
        
        # revert all Z to O
        for i in range(m):
            for j in range(n):
                if board[i][j] == "Z":
                    board[i][j] = "O"