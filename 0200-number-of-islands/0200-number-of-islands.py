def visit(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return

    if grid[i][j] != '1':
        return

    grid[i][j] = 'v'
    
    visit(grid, i + 1, j)
    visit(grid, i - 1, j)
    visit(grid, i, j + 1)
    visit(grid, i, j - 1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    visit(grid, i, j)
        return islands