def count_neighbors(board, m, n, i, j):
    neighbors = 0

    # top-left
    if i > 0 and j > 0:
        neighbors += board[i-1][j-1]

    # left
    if j > 0:
        neighbors += board[i][j-1]

    # top
    if i > 0:
        neighbors += board[i-1][j]
    
    # bottom
    if i < m-1:
        neighbors += board[i+1][j]
        
    # right
    if j < n-1:
        neighbors += board[i][j+1]
    
    # bottom-right
    if i < m-1 and j < n-1:
        neighbors += board[i+1][j+1]
    
    # top-right
    if i > 0 and j < n-1:
        neighbors += board[i-1][j+1]
        
    # bottom-left
    if i < m-1 and j > 0:
        neighbors += board[i+1][j-1]
    
    return neighbors
        
    
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        board_next = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                board_next[i][j] = board[i][j]
        
        for i in range(m):
            for j in range(n):
                nn = count_neighbors(board, m, n, i, j)
                if board[i][j] and nn < 2:
                    board_next[i][j] = 0
                elif board[i][j] and nn in [2, 3]:
                    pass
                elif board[i][j] and nn > 3:
                    board_next[i][j] = 0
                elif not board[i][j] and nn == 3:
                    board_next[i][j] = 1
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board_next[i][j]