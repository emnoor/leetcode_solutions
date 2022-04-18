from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        end = (0, 0)
        non_obstacle_cells = set()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val != -1:
                    non_obstacle_cells |= {(i, j)}

                if val == 1:
                    start = (i, j)
                elif val == 2:
                    end = (i, j)

        m = len(grid)
        n = len(grid[0])

        def trev(i, j, path):
            # we went off the grid, abort mission!!
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0

            # we crossed paths again, oops! :P
            if (i, j) in path:
                return 0

            # obstable :(
            if grid[i][j] == -1:
                return 0

            # we found a path to the end, yay!
            if (i, j) == end:
                return set(path + [(i, j)]) == non_obstacle_cells

            new_path = path + [(i, j)]
            return (
                trev(i - 1, j, new_path)
                + trev(i, j - 1, new_path)
                + trev(i + 1, j, new_path)
                + trev(i, j + 1, new_path)
            )

        return trev(start[0], start[1], [])
